import pymysql

<<<<<<< HEAD
from flask import Blueprint, render_template, request
=======
from flask import Blueprint, render_template, request, redirect, url_for
>>>>>>> ab345c090a80370325e07608551de3670d6d5143

from my_settings import PW

#블루프린트
bp = Blueprint('product', __name__, url_prefix='/product')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()



<<<<<<< HEAD
@bp.route('/<int:product_id>', methods=('GET','POST'))
=======
@bp.route('/<int:product_id>', methods=['GET', 'POST'])
>>>>>>> ab345c090a80370325e07608551de3670d6d5143
#제품 상세페이지
def product(product_id):
    if request.method == 'GET':
        #제품 상세페이지 조회
        try:
            cursor.execute("select * from products where product_id={}".format(product_id))
            products = cursor.fetchall()
            results = [
                {
                    'product_id' : product[0],
                    'name' : product[1],
                    'description' : product[2],
                    'price' : int(product[3]),
                    'delivery_charge' : int(product[4]),
                    'count' : product[5],
                    'tag' : product[6],
                } for product in products
            ]
<<<<<<< HEAD
            return(results), 200
        except:
            return({'message':'실패'})
    elif request.method == 'POST':
    #제품 상세페이지에서 cart 클릭 시 장바구니로 이동
        try:
            products = request.get_json()

            user_id = products['user_id']
            count = products['count']
            
            cursor.execute("insert into cart(user_id, product_id, count) values({},{},{})".format(user_id, product_id, count))
            db.commit()

            return({'message':'성공'})
=======
            return render_template('product.html', results=results), 200
            # return(results), 200
        except:
            # return({'message':'실패'})
            None
    elif request.method == 'POST':
    #제품 상세페이지에서 cart 클릭 시 장바구니로 이동
        try:
            user_id = 3
            product_id = request.form['product_id']
            count = request.form['count']
            
            cursor.execute("insert into cart(user_id, product_id, count) values({},{},{})".format(user_id, product_id, count))
            db.commit()
            
            return redirect(url_for('cart.get', user_id=user_id))
>>>>>>> ab345c090a80370325e07608551de3670d6d5143
        except:
            return({'message':'실패'})
    