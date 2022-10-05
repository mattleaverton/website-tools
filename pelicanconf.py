AUTHOR = 'Matt Leaverton'
SITENAME = 'Matt Leaverton'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
STATIC_PATHS = ['images']

AVATAR_AUTHOR_EMAIL = 'mattleaverton@gmail.com'
HEADLINE = "Software and Electronics Engineer."
CURRENT_COMPANY_POSITION = "Staff Test Systems Software Engineer"
CURRENT_COMPANY_NAME = "Velentium"
CURRENT_COMPANY_LINK = "https://www.velentium.com/"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme"

PLUGINS = ['webassets', 'avatar', 'advthumbnailer']

# Social widget
SOCIAL = (('github', 'mattleaverton'),
          ('linkedin', 'mattleaverton'),)

DEFAULT_PAGINATION = False

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {}
    }
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
