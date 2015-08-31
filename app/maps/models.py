#!/usr/bin/python
from app import db

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    level = db.Column(db.Integer)
    lat = db.Column(db.Numeric)
    lng = db.Column(db.Numeric)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, user_id, level, lat, lng):
        self.user_id = user_id
        self.level = level
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return 'Level %d: (%f, %f)' % (self.level, self.lat, self.lng)

    def __repr__(self):
        return 'Level %d: (%f, %f)' % (self.level, self.lat, self.lng)