#!/usr/bin/python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    user_agent = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, email, user_agent):
        self.email = email
        self.user_agent = user_agent