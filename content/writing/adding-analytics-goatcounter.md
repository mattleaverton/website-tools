Title: Add Web Analytics in 10 Minutes with Goatcounter
Date: 2023-09-03 21:35
Category: Writing
Tags: software, infra
Slug:
Authors: Matt Leaverton
Summary:
Status: published

No exaggeration - it took me 10 minutes or less from deciding to add analytics to my site
with [Goatcounter](https://www.goatcounter.com/) until it was fully setup and deployed.

## Details
Goatcounter is an [open-source](https://github.com/arp242/goatcounter), [privacy friendly](https://www.goatcounter.com/help/privacy),
`free for reasonable public usage`, and ridiculously easy to set up.

I signed up for an account with my email, set the URL of my site, and chose a unique identifier, then I was
all set to go on the Goatcounter side. I only needed to add the following lines to the base HTML template
file for my static site, deploy, and that was absolutely it.

```html
<script data-goatcounter="https://<unique-id>.goatcounter.com/count"
    async src="//gc.zgo.at/count.js"></script>
```

Now I can view page visits over time, get a summary of screen sizes, operating systems, referrals, and country
of origins for views. It even allows me to toggle so that [my own page views do not count](https://www.goatcounter.com/help/skip-dev).
Big fan so far.