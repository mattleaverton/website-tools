
# def project_tag_filter(tag_info):
#     tags = {}
#     for t in tag_info:
#         tag, articles = t
#     print(tags)
#     return "Fancy Tag"


AUTHOR = 'Matt Leaverton'
SITENAME = 'Matt Leaverton'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme"
DEFAULT_PAGINATION = False

# Generation Options
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_SAVE_AS = ''
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

# Social widget
SOCIAL = (('github', 'mattleaverton'),
          ('linkedin', 'mattleaverton'),
          ('twitter', 'mattleaverton'),)

# Content Updates
AVATAR_AUTHOR_EMAIL = 'mattleaverton@gmail.com'
HEADLINE = "Software and Electronics."
CURRENT_COMPANY_POSITION = "Senior Software Engineer"
CURRENT_COMPANY_NAME = "Glowforge"
CURRENT_COMPANY_LINK = "https://www.glowforge.com/"

# JINJA_FILTERS = {
#     'tag_filter': project_tag_filter
# }

CAREER_SUMMARY = 'Placeholder.'
SKILLS = [
    {
        'title': 'Python',
        'level': '90'
    },
    {
        'title': 'C',
        'level': '95'
    },
    {
        'title': 'C++',
        'level': '95'
    },
    {
        'title': 'C#',
        'level': '90'
    },
    {
        'title': 'LabVIEW',
        'level': '85'
    },
    {
        'title': 'Go',
        'level': '85'
    }
]
PROJECT_INTRO = 'You can list your side projects or open source libraries in this section. '
PROJECTS = [
    {
        'title': 'Boids',
        'link': 'https://github.com/mattleaverton/pygame-boids',
        'tagline': 'We make the boids'
    }
]
EXPERIENCES = [
    {
        'job_title': 'Engineer',
        'time': 'Feb 2014 - Present',
        'company': 'Velentium',
        'details': 'Engineering'
    }
]
EDUCATIONS = [
    {
        'degree': 'ECE Degree',
        'meta': 'University of Texas at Austin',
        'time': '2009-2013'
    }
]

# Plugins and Plugin Options
PLUGINS = ['webassets', 'avatar', 'image_process']

IMAGE_PROCESS = {
    "article-image": ["scale_in 600 600 True"],
    "inline": ["scale_in 500 500 True"],
    "thumb": ["scale_out 200 200 True", "crop 0 0 200 200"],
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {}
    }
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
