from flask import Flask
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24) 

print(__name__)

from server import routes