from app.extension import db

class transaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    payment_type = db.Column(db.String(125), nullable='false')
    '''
    def __repr__(self):
        return f'<transaksi {self.payment_type}>'
    '''
