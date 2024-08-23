from app.extension import db

class Transaksi(db.Model):
    __tablename__ = 'transaksi'
    Outlet_Name = db.Column(db.String(225), nullable=False)
    Merchant_Id = db.Column(db.String(225), nullable=False)
    Feature = db.Column(db.String(225), nullable=False)
    Order_Id = db.Column(db.REAL(precision=None, asdecimal=False, decimal_return_scale=None), nullable=True)
    Transaction_Id = db.Column(db.String(225), primary_key=True, nullable=False)
    Amount = db.Column(db.Integer, nullable=False)
    Net_Amount = db.Column(db.Integer, nullable=False)
    Transaction_Status = db.Column(db.String(225), nullable=False)
    Transaction_Time = db.Column(db.DateTime(timezone=True))
    Payment_Type = db.Column(db.String(225), nullable=False)
    Payment_Date = db.Column(db.Date)
    GoPay_Transaction_Id = db.Column(db.String(225))
    GoPay_Reference_Id = db.Column(db.String(225))
    GoPay_Customer_Id = db.Column(db.REAL(precision=None, asdecimal=False, decimal_return_scale=None), nullable=True)
    Qris_Transaction_Type = db.Column(db.String(225))
    Qris_Reference_Id = db.Column(db.String(225))
    Qris_Issuer = db.Column(db.String(225))
    Qris_Acquirer = db.Column(db.String(225))
    Card_Type = db.Column(db.String(225))
    Credit_Card_Number = db.Column(db.REAL(precision=None, asdecimal=False, decimal_return_scale=None), nullable=True)
    Settlement_Date = db.Column(db.Date)
    Settlement_Time = db.Column(db.DateTime(timezone=True))

    def to_dict(self):
        return {
            'Outlet_Name': self.Outlet_Name,
            'Merchant_Id': self.Merchant_Id,
            'Feature' : self.Feature,
            'Order_Id' : self.Order_Id,
            'Transaction_Id' : self.Transaction_Id,
            'Amount' : self.Amount,
            'Net_Amount' : self.Net_Amount,
            'Transaction_Status' : self.Transaction_Status,
            'Transaction_Time' : self.Transaction_Time,
            'Payment_Type' : self.Payment_Type,
            'Payment_Date' : self.Payment_Date.strftime('%Y-%m-%d') if self.Settlement_Date else None,
            'GoPay_Transaction_Id' : self.GoPay_Transaction_Id,
            'GoPay_Reference_Id' : self.GoPay_Reference_Id,
            'GoPay_Customer_Id' : self.GoPay_Customer_Id,
            'Qris_Transaction_Type' : self.Qris_Transaction_Type,
            'Qris_Reference_Id' : self.Qris_Reference_Id,
            'Qris_Issuer' : self.Qris_Issuer,
            'Qris_Acquirer' : self.Qris_Acquirer,
            'Card_Type' : self.Card_Type,
            'Credit_Card_Number' : self.Credit_Card_Number,
            'Settlement_Date' : self.Settlement_Date.strftime('%Y-%m-%d') if self.Settlement_Date else None,
            'Settlement_Time' : self.Settlement_Time
        }