from flask import render_template, request
from app.main import bp

@bp.route('/')
def index():
    return render_template('main/index.html')

@bp.route('/welcome_content')
def welcome_content():
    return render_template('main/welcome_content.html')

@bp.route('/forecast_content')
def forecast_content():
    return render_template('main/forecast_content.html')