from application import db
from flask_login import UserMixin
from datetime import datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField

#Create the Users table
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    
    #What is displayed a part of the object is called
    def __repr__(self):
            return ''.join(['User ID: ', str(self.id), '\r\n',	
                            'Email: ', self.email, '\r\n',
                           'Name: ', self.first_name, ' ', self.last_name])

