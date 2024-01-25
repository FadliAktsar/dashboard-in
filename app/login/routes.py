from flask import render_template, redirect, url_for, request, flash, scalar_one_or_none
from werkzeug.security import generate_password_hash
from app.model.database.user import user
from app.login import bp
from app.extension import db

@bp.route('/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
    username = request.method.get('username')
    password = request.method.get('password')

    excisting_user = db.session.execute(db.select(user).filter_by(username=username)),scalar_one_or_none()
    return render_template('auth/login.html')