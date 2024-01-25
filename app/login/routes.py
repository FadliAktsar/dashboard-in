from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash
from app.login import bp
from app.model.database.user import user as user_model

@bp.route('/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      #remember = True if request.form.get('remember') else False

      user = user_model.query.filter_by(username=username).first()

         # check if the user actually exists
         # take the user-supplied password, hash it, and compare it to the hashed password in the database
      if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login.login')) # if the user doesn't exist or password is wrong, reload the page
      
      return redirect(url_for('main.index'))
                      
   return render_template('auth/login.html')