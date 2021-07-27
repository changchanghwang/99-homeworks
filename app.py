from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보여주기
@app.route('/')
def index():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def order():
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {'name': name_receive,'quantity': quantity_receive,'address': address_receive,'phone': phone_receive}

    db.shopping.insert_one(doc)
    return jsonify({'msg': '주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.shopping.find({},{'_id':False}))
    return jsonify({'view_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)