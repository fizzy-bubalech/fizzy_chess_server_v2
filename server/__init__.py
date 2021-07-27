from flask import Flask
import os
from cachelib.simple import SimpleCache 

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24) 

print(__name__)

c = SimpleCache()

from server import routes