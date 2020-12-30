+++
date = 2020-12-30T22:05:00Z
slug = "Building-a-Personal-Website-for-Free"
title = "Building a Personal Website for Free"

+++
# 📎Why?

Over the years, I set up various blog sites for myself and others using existing services such as Squarespace and WordPress. This year, I want to do something different - making the build process itself a learning journey. It's a good time to do it because of a vast amount of excellent free open-source software available and plenty of tutorials/videos around.

# 📖How?

I have some experience with writing in markdown, working with Python and Git. I used [HUGO](https://gohugo.io/), a [Go](https://golang.org/)-based static site generator to turn my posts in Markdown into HTML, specifically using the minimalist [Cactus theme](https://themes.gohugo.io/hugo-theme-cactus/). For website hosting, I went with [GitHub Pages](https://pages.github.com/). The only thing I paid for was my own domain name [shan.tax](http://shan.tax) from NameCheap.

Most of my blog posts were first done in Apple Notes, and more recently in [Notion](https://www.notion.so). I love how versatile and clean Notion's interface is and started looking into ways of turning Notion pages directly into websites. Unfortunately, Notion has not yet had a public API, so I turned to [Forestry](https://forestry.io/) for content management ("CMS").

Finally, to automate the whole workflow, from drafting a post to publish onto my website, I used [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions) to stitch everything together. The diagram below shows how each process is linked. I'm pleased with the result - a sleek personal website editor built from scratch for free and with decent performance too.

![](/uploads/website_building.png)

# 📮Next?

I dedicated this project to my career-related writing. I'd like to explore more on turning Notion directly into a website. I found some [tutorials](https://blog.kowalczyk.info/article/88aee8f43620471aa9dbcad28368174c/how-i-reverse-engineered-notion-api.html) online which discussed how to reverse engineer a Notion API for this purpose but there are also SaaS (e.g. [Super](https://super.so/)) which claim to serve this purpose. Ideally, I'd like to be able to work with Notion's official API directly but before that, there's plenty for me to get on with✌️