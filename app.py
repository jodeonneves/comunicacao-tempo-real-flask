from flask import Flask, jsonify
from repository.database import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)


@app.route('/payments/pix', methods=['POST'])
def create_payments_pix():
    return jsonify({"message": "The payment has been created"})


@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "The payments has been confirmed"})


@app.route('/payments/pix/<int:payments_id>', methods=['GET'])
def payments_pix_page(payments_id):
    return 'pagamento pix'


if __name__ == '__main__':
    app.run(debug=True)