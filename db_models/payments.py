from repository.database import db


class Payments(db.Model):
    # id, value, paid, bank_payment_id, qrcode, expiration_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qrcode = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)