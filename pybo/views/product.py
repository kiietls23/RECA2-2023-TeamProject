import pymysql

from flask import Blueprint, render_template, request, redirect, url_for, session

from my_settings import PW

#블루프린트
bp = Blueprint('product', __name__, url_prefix='/product')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()



@bp.route('/<int:product_id>', methods=['GET', 'POST'])
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
            return render_template('product.html', results=results), 200
        except:
            return({'message':'실패'})
    elif request.method == 'POST':
    #제품 상세페이지에서 cart 클릭 시 장바구니로 이동
        try:
            if 'email' in session:
                email = session['email']
                cursor.execute("select user_id from users where email='{}'".format(email))
                user_id = cursor.fetchone()[0]
            else:
                return "<script>alert('로그인해라');window.location.replace('/user/log');</script>"
            
            product_id = request.form['product_id']
            count = request.form['count']
            
            cursor.execute("""select c.cart_id, p.name, p.price, p.delivery_charge, c.count, p.description
                    from cart as c join products as p
                    on c.product_id = p.product_id 
                    where c.product_id={} and c.user_id={}
                    """.format(product_id, user_id))
            products = cursor.fetchall()
            
            if len(products) != 0:
                return f"<script>alert('이미 장바구니에 있는 상품입니다');window.location.replace('/cart/{user_id}');</script>"
                
            
            cursor.execute("insert into cart(user_id, product_id, count) values({},{},{})".format(user_id, product_id, count))
            db.commit()
            
            return redirect(url_for('cart.get', user_id=user_id))
        except:
            return "<script>alert('숫자를 입력하시오');javascript:history.back();</script>"
