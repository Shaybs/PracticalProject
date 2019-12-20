from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)

from application import routes
