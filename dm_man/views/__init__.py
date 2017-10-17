from flask import render_template, redirect, request, url_for
from flask_login import LoginManager, login_required
from ..dm import app, db

class Navigation(object):
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption

navigation = [Navigation(href = '/', caption = 'Index'), Navigation(href = '/user', caption = 'Users'), Navigation(href='/projects', caption='Projects')]

__all__ = ['render_template', 'redirect', 'request', 'url_for', 'app', 'db', 'navigation']


