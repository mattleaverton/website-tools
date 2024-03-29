Tooling and raw content for my [Pelican-powered](https://getpelican.com/) GitHub Pages website [mattleaverton.com](https://www.mattleaverton.com)

FYI: prepare site content to publish with:

    pelican content -s publishconf.py

## TODO
- main page to article page shifts alignment of image
- automatically append `{: target=_blank}` to every link
- automatically add/change an update time on article modification
    - mechanism for displaying/explaining later edits 
- the gray bar at the top of the page is thin and can be scrolled above on many platforms
- need cover images for more articles or something - painfully blank
- reading pages need more contrast between sections - everything blends
- update workstation setup and add a picture
- order the books read by updated date
- organize writing directory with sub-folders by year that do not affect the URL
- easier processing of images so that it is quick to grab a screenshot and drop it in
- automatically build and publish from a markdown file commit instead of manual
- fix code blocks for long lines; either word wrap or add an independent scroll bar
- add favicon
- project headline images do not show up in rss
- code blocks have extraneous space at start
- check on image alpha channel support (with the static site image optimizer)
- reading table formatting in rss is terrible

## Acknowledgements
Based on the [Pelican simple theme](https://github.com/getpelican/pelican/tree/master/pelican/themes/simple/templates)

Thanks to:
* [Mitxela](https://mitxela.com/projects/hardware) for the project page layout inspiration
* [Karambir Singh Nain](https://github.com/karambir/taman) for the Taman pelican theme, which introduced me to the ideas below
* [Giulio Fidente](https://github.com/gfidente/pelican-svbhack) for several template starters and introduction to [Skeleton CSS](http://getskeleton.com/)
* [Daniel Berkompas](https://blog.danielberkompas.com/) for the article listing inspiration
* [Matt Swanson](https://mdswanson.com/) for general layout inspiration
* [Suhaib Khan](https://github.com/suheb/resume), [Sharath Kumar](https://github.com/sharu725/online-cv), and [Xiaoying Riley](https://themes.3rdwavemedia.com/bootstrap-templates/resume/orbit-free-resume-cv-bootstrap-theme-for-developers/) for the template and design inspiration for the CV page