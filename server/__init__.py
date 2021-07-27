from flask import Flask
import os
from flask_caching import Cache

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24) 
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)

print(__name__)

c = Cache(app)

from server import routes