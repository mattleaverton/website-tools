Title: Python EXE Debugging Trick
Date: 2022-10-15 21:35
Category: Writing
Tags: software, python
Slug:
Authors: Matt Leaverton
Summary:
Status: published
Github: https://github.com/mattleaverton/py-exe-debugging


Debugging unexpected behavior in an executable - typically using [PyInstaller](https://pyinstaller.org/en/stable/){: target=_blank}.

Thanks to Jason R. Coombs and Steven Kryskalla in [this StackOverflow answer](https://stackoverflow.com/a/1396386){: target=_blank} from
2009 for this excellent nugget.

    :::python
    import code
    code.interact(local=locals())

Debugging path and import errors


