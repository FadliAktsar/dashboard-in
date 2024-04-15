from flask import render_template, request, flash
#from flask_login import login_required, current_user
from app.dashboard import bp

@bp.route('/', methods=['GET', 'POST'])
#@login_required
def index(): 
    return render_template('dashboard/index.html')
