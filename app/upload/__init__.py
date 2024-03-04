from flask import Blueprint

bp = Blueprint('penjualan', __name__)

from app.upload import routes