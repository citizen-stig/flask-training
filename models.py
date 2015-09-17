# -*- encoding: utf-8 -*-
# apps.members.models
from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy import db.Column, db.Integer, db.String, DateTime, Boolean, Float

db = SQLAlchemy()


class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), nullable=False)
	last_name = db.Column(db.String, nullable=False)
	email = db.Column(db.String)
	password = db.Column(db.String,	nullable=True)

	def __str__(self):
		return "{0} {1}".format(self.first_name, self.last_name)


class Manufacturer(db.Model):
	__tablename__ = "manufacturers"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	country = db.Column(db.String, nullable=False)
	# db.relationship('Car', backref='manufacturer', lazy='dynamic')

	def __str__(self):
		return self.name


class Car(db.Model):
	__tablename__ = "cars"
	id = db.Column(db.Integer, primary_key=True)
	model = db.Column(db.String, nullable=False)
	manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'))

	def __str__(self):
		return self.manufacturer.name + ' ' + self.model



