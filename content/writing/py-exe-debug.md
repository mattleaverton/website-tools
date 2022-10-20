Title: Python EXE Debugging Trick
Date: 2022-10-19 21:35
Category: Writing
Tags: software, python
Slug:
Authors: Matt Leaverton
Summary:
Status: published
Github: https://github.com/mattleaverton/py-exe-debugging

There comes a time in every Python developer's life when they are ready for the next level: freezing scripts into
an EXE for deployment. Much ink and blood has been shed on the topic and I have nothing to contribute directly to that
today other than [PyInstaller](https://pyinstaller.org/en/stable/){: target=_blank} is a very reasonable tool for the
job.

If you are still reading after that earth-shattering news, you are in for a treat. Not long after the aforementioned time comes,
another time comes along - the EXE does not work, and you are stumped.

Thanks to Jason R. Coombs and Steven Kryskalla in [this StackOverflow answer](https://stackoverflow.com/a/1396386){: target=_blank} from
2009, here is an excellent software nugget that can ease debugging particularly sticky PyInstaller issues.

    :::python
    import code
    code.interact(local=locals())

With no external libraries or fancy code, this drops you directly into the Python REPL (Read Evaluate Print Loop).
This should feel familiar as it is rather like the standard Python command line interface, which makes for a powerful 
debugging tool for a frozen environment. 

A couple notes: 

- **First**, nothing is imported by default, so import everything you want
to use. 
- **Second**, when frozen, only the bundled libraries are available for access so not Python library installed locally
on your system will be available. The Python standard library is bundled in with PyInstaller - run `sys.builtin_module_names`
(after importing sys) to see what is available. 
- **Third**, especially if using PyInstaller in `--onefile` mode, paths 
get complicated, so take care to understand where you are and where things are relative to you if that is 
important to your debugging. 
- **Last**, simply use `sys.exit()` to exit when finished - make sure to import sys first.


---

To see how this can assist in debugging, consider the following scenario: you are developing a script to help a bakery 
advertise their delicious foods. This script was not developed with deployment in mind, but you have people 
showing interest, and you wish to share an EXE. The script works just fine when run it on your machine in test mode: 

    Welcome to Buntastic Bakery - please enjoy your 'Placeholder Croissant'

So you say, great, bundle it into an EXE and ship it to your dozens of friends who enjoy fine baked goods. 

Soon, reports are rolling in that instead of information about fine baked confections, your friends are getting the 
unappetizing test message:
    
    Welcome to Buntastic Bakery - please enjoy your 'Crusty Test Croissant'

Apparently you neglected to run the EXE before shipping, because you see the same message on your machine when
you test. Time to debug. With test mode enabled, the message should come from `place_holder_baked_good` so that 
[seems like a good place to start looking](https://github.com/mattleaverton/py-exe-debugging/blob/main/data/data_manager.py#L13){: target=_blank}. 

Adding the code snippet from above to the code yields the following:

    :::python
    def placeholder_baked_good(confection: str) -> str:
        """ Test mode - find and return a test baked good """

        import code
        code.interact(local=locals())

        baked_good = importlib.import_module('library.test_data')
        return baked_good.TEST_STRING.format(confection)

> **Note:** Play along at home with this code by getting your own copy [from Github](https://github.com/mattleaverton/py-exe-debugging){: target=_blank} 

Build into an EXE and run it again to find yourself in the interactive Python console

    :::python
    > pyinstaller main.spec
    > .\dist\main.exe
    Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> 

The invalid output message indicates that the code inside the `ModuleNotFoundError` exception is run, so test out
the import manually to see if that is in fact the issue.

    :::python
    >>> import library.test_data as baked_good
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    ModuleNotFoundError: No module named 'library'

As suspected - Python reports that it cannot find our `library` module. It is clearly present in the repo and this code
works when run in script format, so something must be missing when translating into the EXE. One last check to confirm - 
`sys.modules` shows all modules that the Python import system and PyInstaller module loaders have found and processed
(as noted before, if you're looking for built-in libraries, use `sys.builtin_module_names`). If the package you
want to import is not shown in `sys.modules` then Python has not seen the library we are looking for yet.

    :::python
    >>> import sys
    >>> from pprint import pprint
    >>> pprint(sys.modules)
    ...
    'copyreg': <module 'copyreg' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\base_library.zip\\copyr...
    'data': <module 'data' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\data\\__init__.pyc'>,
    'data.data_manager': <module 'data.data_manager' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\dat...
    'dataclasses': <module 'dataclasses' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\dataclasses.pyc...
    ...
    'io': <module 'io' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\base_library.zip\\io.pyc'>,
    'itertools': <module 'itertools' (built-in)>,
    'keyword': <module 'keyword' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\base_library.zip\\keywo...
    'linecache': <module 'linecache' from 'C:\\Users\\MATTLE~1\\AppData\\Local\\Temp\\_MEI175642\\base_library.zip\\l...
    'marshal': <module 'marshal' (built-in)>,
    ...

First, you can see that the `data` and `data.data_manager` modules where the `placeholder_baked_good` and `get_baked_good` 
methods are located are already processed - PyInstaller found those and brought them along. You can also see
that `library` is completely missing.

PyInstaller can perform a lot of magic in deciding what to bundle, but it is not perfect. This example case is 
contrived to deliberately bamboozle PyInstaller with a dynamic import that it cannot see. It demonstrates
that if your use case requires code trickery, care must be taken to give PyInstaller its best chance at success.

In this case, the solution is simple - give PyInstaller a hand by adding `library.test_data` to the `hiddenimports` list 
in `main.spec`:
    
    :::python
    a = Analysis(
        ['main.py'],
        pathex=[],
        binaries=[],
        datas=[],
        hiddenimports=['library.test_data'],
        cipher=None,
        noarchive=False,
    )
    pyz = PYZ(a.pure, a.zipped_data, cipher=None)

Upon removal of the debug code and a rebuild, the EXE now works as expected.

    :::python
    > pyinstaller main.spec
    > .\dist\main.exe
    Welcome to Buntastic Bakery - please enjoy your 'Placeholder Croissant'

Astute readers may note - the simplest solution to the exact problem presented is to remove the
dynamic import and place `from library import test_data as baked_good`, which will work and also hint to PyInstaller
to bring along `library.test_data` with no extra help. Let this serve as both a recommendation to try to work with
PyInstaller as often as possible, but also a way to get out of sticky situations if you need it. 

---

A neat PyInstaller specific trick to see exactly what modules could be available for import, and not just those processed 
already is to dig into the custom importers that PyInstaller creates to load code from the EXE archive it creates.
Anyone can write extensions Python import system, details of which are for another day. The "path finders" - used
to process an import statement and determine if there is anything available to load - can be viewed at `sys.meta_path`:

    :::python
    >>> sys.meta_path
    [<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, 
     <pyimod02_importers.FrozenImporter object at 0x000002172DA54DF0>, <class '_frozen_importlib_external.PathFinder'>]

`pyimod02_importers.FrozenImporter` here is the PyInstaller path finder responsible for reporting whether an import
statement can load any module from its bundle. On load, this finder [builds a table of contents](https://github.com/pyinstaller/pyinstaller/blob/develop/PyInstaller/loader/pyimod02_importers.py#L117){: target=_blank} containing all available 
libraries, and we can take a peek:

    :::python
    >>> import sys
    >>> from pprint import pprint
    >>> pprint(sys.meta_path[2].toc)
    ...
    'importlib.util',
    'inspect',
    'library',
    'library.test_data',
    'logging',
    'lzma',
    'mimetypes',
    ...
    >>> import library.test_data as baked_good
    >>> print(baked_good.TEST_STRING.format("Muffin"))
    Placeholder Muffin

After fixing our dynamic import issue, `library.test_data` is now available and can be successfully imported and used.

---

PyInstaller provides [several official solutions](https://pyinstaller.org/en/stable/when-things-go-wrong.html){: target=_blank} 
to problematic scenarios. In case those do not fit your needs, let this trick be another
tool in your belt for debugging deployments. 
