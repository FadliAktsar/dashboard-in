from flask import render_template
from app.penjualan import bp

@bp.route('/')
def index():
    
    return render_template('penjualan/index.html')
