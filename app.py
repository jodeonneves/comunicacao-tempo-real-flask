from flask import Flask, jsonify, request, send_file
from repository.database import db
from db_models.payments import Payments
from datetime import datetime, timedelta
from payments.pix import Pix


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # variavel de configuração, obrigtoria
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'  # variavel de configuração, obrigtoria

db.init_app(app)


@app.route('/payments/pix', methods=['POST'])
def create_payments_pix():
    data = request.get_json()

    # validações
    if 'value' not in data:
        return jsonify({"message": "Invalid value"}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payments(value=data['value'], expiration_date=expiration_date)

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payments()
    new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]
    new_payment.qrcode = data_payment_pix["qr_code_path"]

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({"message": "The payment has been created",
                   "payment": new_payment.to_dict()})



@app.route('/payments/pix/qr_code/<file_name>', methods=["GET"])
def get_image(file_name):
    return send_file(f"static/img/{file_name}.png", mimetype='image/png')


@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payments has been confirmed"})


@app.route('/payments/pix/<int:payments_id>', methods=['GET'])
def payments_pix_page(payments_id):
    return 'pagamento pix'


if __name__ == '__main__':
    app.run(debug=True)