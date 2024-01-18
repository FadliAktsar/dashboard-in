from flask import render_template
from app.peramalan import bp

@bp.route('/peramalan')
def peramalan():
    return render_template('peramalan.html')
