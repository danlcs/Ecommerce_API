from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    

@app.route('/api/products/add', methods=['POST']) # Definir rota para página de adição de produtos e função que a executa
def add_product():
    if 'name' in data and 'price' in data:
        data = request.json
        product = Product(name=data['name'], price=data['price'], description=data.get('description', 'ERRO'))
        db.session.add(product)
        db.session.commit()
        return jsonify({'message':'Product added successfully'}), 200
    return jsonify({'message': 'Invalid data, missing price or name'}), 400

@app.route('/') # Definir uma rota raiz (pág. inicial) e a função que será executada ao requisitar
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)