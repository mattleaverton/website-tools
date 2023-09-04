Title: Font Size Bookmarklet
Date: 2023-04-12 21:35
Category: Writing
Tags: software, til
Slug:
Authors: Matt Leaverton
Summary:
Status: draft

Messing around with bookmarklets and found this handy bookmarklet editor with some example
bookmarklets [here at Gibney.org](https://www.gibney.org/bookmarklet_editor){: target=_blank}.
I've been using the `Increase Font Size` one regularly when a site's text is too small
to read comfortably - this increases the size of all fonts on the page by 25% every time you click on it.

From the site linked above - here is the base javascript:

```javascript
let elms = [...document.querySelectorAll('*')];

for (let elm of elms) {
    let cs = getComputedStyle(elm);
    let fs = cs['font-size'];
    elm.oriSize = parseFloat(fs);
}

for (let elm of elms) {
    let fs = 1.25 * elm.oriSize;
    elm.style.fontSize = fs + "px";
}
```

And here is the bookmarklet version - make a new browser bookmark and set the following as the URL:

```javascript
javascript:(function()%7Blet%20elms%20%3D%20%5B...document.querySelectorAll('*')%5D%3B%0A%0Afor%20(let%20elm%20of%20elms)%20%7B%0A%20%20%20%20let%20cs%20%3D%20getComputedStyle(elm)%3B%0A%20%20%20%20let%20fs%20%3D%20cs%5B'font-size'%5D%3B%0A%20%20%20%20elm.oriSize%20%3D%20parseFloat(fs)%3B%0A%7D%0A%0Afor%20(let%20elm%20of%20elms)%20%7B%0A%20%20%20%20let%20fs%20%3D%201.25%20*%20elm.oriSize%3B%0A%20%20%20%20elm.style.fontSize%20%3D%20fs%20%2B%20%22px%22%3B%0A%7D%7D)()
```
