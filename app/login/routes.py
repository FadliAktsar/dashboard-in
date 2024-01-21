from flask import render_template,request,flash, redirect, url_for
from app.login import bp

@bp.route('/login', methods=['GET, POST'])
def login():
    if request.methods == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = db.session.execute(
            db.select(users).filter_by(username=username)).scalar_one_or_none()
        if users:
            if check_password_hash(users.password, password):
                flash('Login berhasil!', category='success')
                login_user(users, remember=True)

                existing_preferences = db.session.execute(
                    db.select(Preference).filter(Preference.user_id=current_user.id)).scalars().all()
                if existing_preferences:
                    return redirect(url_for('main.'))

    return render_template('login.html')
