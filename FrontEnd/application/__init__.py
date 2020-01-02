from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
#from application.models import db
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("MYSQL_URL")+"/"+os.getenv("MYSQL_DB")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.app_context().push()
db.init_app(app)
db.create_all()

from application import routes
