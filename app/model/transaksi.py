from app.extension import db

class Transaksi(db.Model):
    __tablename__ = 'transaksi'
    Outlet_Name = db.Column(db.String(225), nullable=False)
    Merchant_Id = db.Column(db.String(225), nullable=False)
    Feature = db.Column(db.String(225), nullable=False)
    Order_Id = db.Column(db.String(225))
    Transaction_Id = db.Column(db.String(225), nullable=False)
    Amount = db.Column(db.Integer, nullable=False)
    Net_Amount = db.Column(db.Integer, nullable=False)
    Transaction_Status = db.Column(db.String(225), nullable=False)
    Transaction_Time = db.Column(db.DateTime(timezone=True))
    Payment_Type = db.Column(db.String(225), nullable=False)
    Payment_Date = db.Column(db.Date)
    GoPay_Transaction_Id = db.Column(db.String(225))
    GoPay_Reference_Id = db.Column(db.String(225))
    Gopay_Customer_Id = db.Column(db.Integer)
    Qris_Transaction_Type = db.Column(db.String(225))
    Qris_Reference_Id = db.Column(db.String(225))
    Qris_Issuer = db.Column(db.String(225))
    Qris_Acquirer = db.Column(db.String(225))
    Card_Type = db.Column(db.String(225))
    Credit_Card_Number = db.Column(db.Integer, nullable=True)
    Settlement_Date = db.Column(db.Date, nullable=True)
    Settlement_Time = db.Column(db.DateTime(timezone=True))

