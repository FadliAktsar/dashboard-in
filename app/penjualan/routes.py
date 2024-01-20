from flask import render_template
from app.penjualan import bp

@bp.route('/penjualan')
def penjualan():
    return render_template('penjualan.html')
