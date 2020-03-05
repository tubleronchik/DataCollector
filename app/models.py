#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import db

class Data(db.Model):
    #create a table
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    age = db.Column(db.Integer)
    country = db.Column(db.String)
    db.create_all()

    def __init__(self, age, country): #constructor for a class
        self.age = age
        self.country = country
