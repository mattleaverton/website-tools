Title: Enable IPv6 on Asuswrt-Merlin Router
Date: 2023-07-30 21:35
Category: Writing
Tags: software
Slug:
Authors: Matt Leaverton
Summary:
Status: published

Recently I started using [Vultr](https://www.vultr.com/){: target=_blank} for VPS hosting ([details here]({filename}/vultr-for-vps.md){: target=_blank})
and the cheapest instance is IPv6 only. This suits my purposes just fine, except that I was unable to SSH into the 
server from my home network. I could not even ping it successfully.

From research, I learned that many routers have IPv6 disabled by default, including my Asus router running Asuswrt-Merlin.
[This help article from Asus](https://www.asus.com/support/FAQ/113990/){: target=_blank} did the trick. After updating my
`Connection Type` from the `Advanced Settings -> IPv6` menu from `Disable` to `Native`, I was good to go. My local computer
now had an IPv6 address and I could ping and SSH an IPv6 address to my heart's content

