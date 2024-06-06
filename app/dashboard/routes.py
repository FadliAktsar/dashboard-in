from flask import render_template, request, flash
from app.extension import db
from app.dashboard import bp

@bp.route('/', methods=['GET', 'POST'])
#@login_required
def index():
     
    return render_template('dashboard/index.html')
