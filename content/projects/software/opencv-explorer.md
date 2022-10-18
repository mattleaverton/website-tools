Title: OpenCV Explorer
Date: 2021-11-11 22:18
Modified: 2022-09-05 22:18
Category: Projects
Tags: software, opencv, python
Slug:
Authors: Matt Leaverton
Summary: Simplify prototyping in OpenCV
Status: published
Phase: Design
Github: https://github.com/mattleaverton/opencv-explorer
Cover: images/cv-explorer-demo.jpg

There is nothing more 

### View:
- Live view 
- Toggle to raw view (unprocessed); side-by-side?
- Intermediate image views assignable (pack the images in and organize together)
- Pan, Zoom available and controllable with mouse, keyboard, finger

### Editor:
- All opencv methods available
- Useful or regular usage items assigned shortcut names
- Certain useful functions aliased for quick use (resize, to black and white, save to file)
- Can use unix -x or list args in order
- Can take video or image sources as input
- Syntax errors are noted on a line and ignored (rest of script unaffected)
- Variable assignment (save this output for use later by name)
	- Indexable for multi-output methods?
	- Raw image is auto assigned a variable like %RAW% or similar
- Show line numbers
- Swap lines, duplicate lines, delete, cut/paste whole lines from keyboard shortcuts

### Help / Learn:
- Searchable knowledge base of methods and syntax
- Show info about active command in the editor
- Browseable compendium of all opencv commands with description, args, and shortcuts (if applicable)

### Factory / Filter / Modifier:
- Group all objects together in a folder
- File per modifier (opencv command)
- Object handles syntax, argument distribution, inputs/outputs
- Object handles code generation
- Need a destruct for when it is removed (e.g. stop video capture)

### Export
- Code generation on demand (Python)
