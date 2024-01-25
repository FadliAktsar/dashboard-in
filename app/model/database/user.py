from app.extension import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key='True')
    username = db.Column(db.String(125), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(125), nullable=False)

    def __repr__(self):
        return f'<user {self.username}>'
