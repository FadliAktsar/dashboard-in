from app.extension import db

class Peramalan(db.Model):
    __tablename__ = 'peramalan'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Settelement_Date = db.Column(db.Date, nullable=False)
    Forecast = db.Column(db.Integer, nullable=False)
    Revenue = db.Column(db.Integer, nullable=False)