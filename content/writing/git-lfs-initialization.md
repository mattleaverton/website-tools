Title: Initialize Git LFS
Date: 2023-07-31 21:35
Category: Writing
Tags: software, til
Slug:
Authors: Matt Leaverton
Summary:
Status: published

So I can remember how to do this in the future.

Enable Git LFS on a repo:

- clone empty repo, master branch
- cd into repo directory

``` commandline
git lfs install
git lfs track "*.png" "*.PNG" "*.jpg" "*.JPG" "*.jpeg" "*.JPEG" "*.zip" "*.ZIP" "*.db" "*.DB"
git add .gitattributes
git commit -m "Add LFS support to repo"
git push
git lfs push origin master
git lfs pull
```

- repeat above for each existing branch
- manually update `.gitattributes` in future to add more file filters as necessary


Thanks to my friend [CW](https://www.ipdb.org/search.cgi){: target=_blank} for the instructions.
