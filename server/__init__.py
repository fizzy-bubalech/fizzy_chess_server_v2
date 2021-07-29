from flask import Flask
import os
from pathlib import Path

from server.common import cache, cache1, games_cache

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24) 

cache.init_app(app=app, config={"CACHE_TYPE": "filesystem",'CACHE_DIR': Path('/tmp/cache')})

cache1.init_app(app=app, config={"CACHE_TYPE": "filesystem",'CACHE_DIR': Path('/tmp/cache1')})

games_cache.init_app(app=app, config={"CACHE_TYPE": "filesystem",'CACHE_DIR': Path('/tmp/gamesCache')})



print(__name__)


from server import routes