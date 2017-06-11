#!/usr/bin/env python
from flask import Flask


app = Flask(__name__)

from app.db.database import init_db
init_db()

from app import views
