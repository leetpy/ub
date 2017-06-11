#!/usr/bin/env python
from sqlalchemy import Column, Integer, String
from app.db.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))
    name = Column(String(120))

    def __init__(self, email, password, name=None):
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.email

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Node(Base):
    __tablename__ = 'nodes'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(60), unique=True)
    name = Column(String(120))

    def __init__(self, uuid, name=None):
        self.uuid = uuid
        self.name = name

    def to_josn(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}