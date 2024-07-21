from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user

from werkzeug.security import check_password_hash

from app.models.user import User
from app.auth import bp

@bp.route('/login', methods=['POST'])
def login():
   return render_template('auth/login.html')

@bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    #remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

      # if the above check passes, then we know the user has the right credentials
    #login_user(user, remember=remember)
    return redirect(url_for('main.index'))