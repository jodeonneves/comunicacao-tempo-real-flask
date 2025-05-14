from repository.database import db


class Payments(db.Model):
    # id, value, paid, bank_payment_id, qrcode, expiration_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qrcode = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_pay,emt_id": self.bank_payment_id,
            "qrcode": self.qrcode,
            "expiration_date": self.expiration_date
        }