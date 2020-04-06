from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #1. 정보를 잘 받자. 제목, 내용, 리뷰
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    # 2. DB에 저장
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'number': number_receive
    }
    db.orders.insert_one(doc)

    # 3. 잘 되었음을 클라이언트에게 알려주자
    return jsonify({'result':'success', 'msg': '주문이 성공적으로 저장되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    #1. 정보를 가져온다.
    orders = list(db.orders.find({}, {'_id': 0}))
    #2. 리뷰들을 돌려준다.
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)