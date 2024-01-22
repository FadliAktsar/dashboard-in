from flask import render_template
from app.peramalan import bp

@bp.route('/')
def index():
    return render_template('peramalan/index.html')
