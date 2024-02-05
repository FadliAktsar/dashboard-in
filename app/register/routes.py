from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
from app.model.user import user
from app.register import bp
from app.extension import db

@bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        # Menggunakan objek User yang di-import dari model
        existing_user = user.query.filter((user.username == username) | (user.email == email)).first()

        if existing_user is None:
            # Membuat objek User baru
            new_user = user(
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