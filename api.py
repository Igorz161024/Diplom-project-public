from flask import Flask, jsonify, request

app = Flask(__name__)

# Тимчасові дані (поки без бази)
users = []
products = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added", "user": data}), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    products.append(data)
    return jsonify({"message": "Product added", "product": data}), 201

if __name__ == '__main__':
    app.run(debug=True)