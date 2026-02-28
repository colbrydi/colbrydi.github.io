"""
Pelican publishing configuration.

This file contains settings used when publishing the site to production.
"""

# This file is used for production settings and overrides pelicanconf.py
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: E402, F401, F403

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://yourdomain.com"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
