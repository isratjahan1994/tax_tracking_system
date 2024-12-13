from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

payments = []

@app.route('/')
def index():
    """Route to render the main page."""
    return render_template('index.html')

@app.route('/view_payments', methods=['GET'])
def view_payments():
    """Return the list of payments as JSON."""
    return jsonify(payments)

@app.route('/add_payment', methods=['POST'])
def add_payment():
    """Add a payment to the in-memory database."""
    data = request.get_json()
    new_payment = {
        'id': len(payments) + 1,
        'company': data.get('company'),
        'amount': data.get('amount'),
        'payment_date': data.get('payment_date'),
        'status': data.get('status'),
        'due_date': data.get('due_date')
    }
    payments.append(new_payment)
    return jsonify({'message': 'Payment added successfully!'})

@app.route('/delete_payment/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    """Delete a payment by its ID."""
    global payments
    payments = [payment for payment in payments if payment['id'] != payment_id]
    return jsonify({'message': f'Payment with ID {payment_id} deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
