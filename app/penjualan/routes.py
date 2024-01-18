from flask import render_template
from app.penjualan import bp

@bp.route('/penjualan')
def peramalan():
    return render_template('penjualan.html')
