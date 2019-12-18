from flask import Flask, request
import requests
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("MYSQL_URL")+"/"+os.getenv("MYSQL_DB")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap(app)

from application import routes
