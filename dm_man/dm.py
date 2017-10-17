"""Entry point to web app config"""
import os
from flask import Flask
from .config import app_config
from .models import db

def create_app(config):
    """Create athe app attribute using config"""
    app = Flask(__name__)
    app.config.from_object(app_config[config])
    app.config.from_pyfile('config.py')
    app.config['MONGOALCHEMY_DATABASE'] = 'newdb'
    app.config['MONGOALCHEMY_SERVER'] = os.environ['DB_PORT_27017_TCP_ADDR']

    db.init_app(app)
    return app

config_name = os.getenv('APP_SETTINGS', 'development')
app = create_app(config_name)

import dm_man.views
import dm_man.views.user_view
import dm_man.views.index
import dm_man.views.project_view
