from flask import render_template, request, flash
#from flask_login import login_required, current_user
from app.peramalan import bp



@bp.route('/', methods=['GET', 'POST'])
#@login_required
def index(): 
    return render_template('peramalan/index.html')
