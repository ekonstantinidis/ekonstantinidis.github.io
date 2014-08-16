#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Emmanouil Konstantinidis'
SITENAME = u'I am Emmanouil'
SITEURL = 'http://www.iamemmanouil.com'

# Document-relative URLs when developing
RELATIVE_URLS = True

PATH = 'content'

DEFAULT_DATE_FORMAT = ' %Y %a %d %B'
TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Menu
MENUITEMS = (
    ('About', '/about/'),
    ('Home', '/'),
    ('Get in touch', 'get-in-touch'),
)

# Theme
OUTPUT_PATH = "output"
THEME = "theme"
THEME_STATIC_DIR = "static"


# Pages Settings
PAGE_URL = "{slug}"
PAGE_SAVE_AS = 'pages/{slug}.html'

# Articles Settings
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = '{slug}.html'

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('fa-twitter', 'http://twitter.com/ekondis'),
    ('fa-github', 'http://github.com/ekonstantinidis'),
    ('fa-linkedin', 'http://uk.linkedin.com/in/ekonstantinidis'),
    ('fa-rss', '#'),
)

DEFAULT_PAGINATION = 5

# Google Analytics
GOOGLE_ANALYTICS= "UA-6891078-38"

# Disqus Comments
DISQUS_SITENAME = "iamemmanouil"

# Twitter Settings
TWITTER_USERNAME = "ekondis"
