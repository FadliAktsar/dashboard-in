from flask import render_template, redirect, url_for, request, flash
#from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app.extension import db
from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')

      user = User.query.filter_by(username=username).first()

         # Mengecek apakah user telah terdaftar
         # take the user-supplied password, hash it, and compare it to the hashed password in the database
      if not user or not check_password_hash(user.password, password):
            flash('User Tidak Terdaftar Atau Password Tidak Cocok.')
            return redirect(url_for('auth.login'))
      #login_user(user, remember=remember)
      return redirect(url_for('main.index'))
                      
   return render_template('auth/login.html')

'''
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    '''