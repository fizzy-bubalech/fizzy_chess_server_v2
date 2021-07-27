from flask import Flask
import os
from cachelib.base import BaseCache 

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24) 

print(__name__)

c = BaseCache()

from server import routes