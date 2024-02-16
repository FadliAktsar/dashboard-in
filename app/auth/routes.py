from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app.model.user import User
from app.extension import db
from app.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      #remember = True if request.form.get('remember') else False

      user = User.query.filter_by(username=username).first()

         # check if the user actually exists
         # take the user-supplied password, hash it, and compare it to the hashed password in the database
      if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login.login')) # if the user doesn't exist or password is wrong, reload the page
      
      return redirect(url_for('main.index'))
                      
   return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        # Menggunakan objek User yang di-import dari model
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

        if existing_user is None:
            # Membuat objek User baru
            new_user = User(
                username=username,
                email=email,
                password=generate_password_hash(password, method='scrypt')
            )
            db.session.add(new_user)
            db.session.commit()

            flash('Registrasi berhasil.', category='success')
            return redirect(url_for('login.login'))
        
        elif len(username) < 2:
            flash('Username harus lebih dari 1 karakter!', category='error')
        elif len(email) < 4:
            flash('Email harus lebih dari 4 karakter!', category='error')
        elif len(password) < 8:
            flash('Password harus lebih dari 8 karakter!', category='error')
        elif password != password_confirmation:
            flash('Password tidak sesuai!', category='error')
        else:
            flash('Username atau Email sudah terdaftar', category='danger')
    
    return render_template('auth/register.html')