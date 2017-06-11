#!/usr/bin/env python
import json
from flask import redirect, sessions, url_for, request, g, send_file, jsonify, Response
from app import app
from app.db.database import db_session
from app.object.models import User


@app.route('/')
@app.route('/index')
def index():
    return send_file('templates/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_obj = json.loads(request.data)
        if check_user(user_obj.get("email"), user_obj.get("password")):
            return "OK", 200
        else:
            return "Failed", 401
    else:
        return send_file('templates/login.html')


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/api/users', methods=['GET'])
def get_users():
    result = User.query.all()
    users_list = [each.to_json() for each in result]
    users = {'users': users_list}
    resp = Response(response=json.dumps(users),
                    status=200,
                    mimetype="application/json")
    return resp


@app.route('/user', methods=['GET', 'POST'])
def user():
    # u = User('liekkas@gmail.com', '123', 'admin')
    # db_session.add(u)
    # db_session.commit()

    # qu = User.query.all()
    return send_file('templates/user.html')


def logout_user():
    pass


def check_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        return True
    return False
