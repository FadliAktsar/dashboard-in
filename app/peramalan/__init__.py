from flask import Blueprint

bp = Blueprint('peramalan', __name__)

from app.peramalan import routes