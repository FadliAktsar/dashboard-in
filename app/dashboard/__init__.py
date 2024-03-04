from flask import Blueprint

bp = Blueprint('peramalan', __name__)

from app.dashboard import routes