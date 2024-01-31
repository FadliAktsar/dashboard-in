from app.extension import db

class peramalan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    label = db.Column(db.String(125), nullable='false')