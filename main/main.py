from dataclasses import dataclass

import requests
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from producer import publish
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@10.244.1.37/main'
CORS(app)

db = SQLAlchemy(app)
@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    
@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products') 
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/sub', methods=['POST'])

def sub(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    json = req.json()

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_subed', id)
    except:
        abort(400, 'You already subscribed to this product')


    return jsonify({
        'message': 'success'
    })

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
