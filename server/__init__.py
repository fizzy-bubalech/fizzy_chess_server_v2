from flask import Flask
import os
from cachelib.file import FileSystemCache 

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24) 

print(__name__)

c = FileSystemCache('/localCache')

from server import routes