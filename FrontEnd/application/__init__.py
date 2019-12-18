from flask import Flask, request
import requests
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from application import routes
