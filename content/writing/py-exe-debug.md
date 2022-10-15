Title: Debug Python EXE
Date: 2022-10-15 21:35
Category: Writing
Tags: software, python
Slug:
Authors: Matt Leaverton
Summary:
Status: published


Debugging unexpected behavior

Thanks to Jason R. Coombs and Steven Kryskalla in [this StackOverflow answer](https://stackoverflow.com/a/1396386) from
2009 for this excellent nugget.

    :::python
    import code
    code.interact(local=locals())

Debugging path and import errors


