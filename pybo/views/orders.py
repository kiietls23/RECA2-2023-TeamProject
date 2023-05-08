import pymysql
from flask import Blueprint, render_template, request, url_for, redirect, flash
from my_settings import PW

#블루프린트
bp = Blueprint('orders', __name__, url_prefix='/orders')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()

@bp.route('/<int:user_id>/<products>', methods=('GET', 'POST'))
# 장바구니에서 가져온 결제 정보 조회(payments, products 테이블)
def get(user_id, products):
    if request.method == 'GET':
        try:
            products = products.split(',') 
            if len(products) == 1:
                product = int(products[0])
                cursor.execute("""select c.cart_id, p.name, p.price, p.delivery_charge, c.count, p.description
                            from cart as c join products as p
                            on c.product_id = p.product_id 
                            where c.product_id={} and c.user_id={}
                            """.format(product, user_id))
            else:
                product =  [int(i) for i in products]
                product = tuple(product)
                cursor.execute("""select p.product_id, p.name, p.price, p.delivery_charge, c.count
                            from cart as c join products as p
                            on c.product_id = p.product_id 
                            where c.product_id in {} and c.user_id={}
                            """.format(product, user_id))
            carts = cursor.fetchall()
            payments = [
                {
                    'product_id': cart[0],
                    'count' : int(cart[4]),
                    'name': cart[1],
                    'price': int(cart[2]),
                    'delivery_charge': int(cart[3]),
                    'total_price' : int((cart[2]*cart[4])+cart[3])
                } for cart in carts
            ]

            if len(payments) == 0:
                return("결제할 상품이 없음"), 200
            else:
                item_count = 0
                sum_total = 0

            # 총 합계 금액 sum_total과 결제할 상품 개수 item_count 계산
            for p in payments:
                sum_total += p['total_price']
                item_count += 1

            # 주문자 정보 조회
            cursor.execute("select name, email, address, phone from users where user_id={};".format(user_id))
            user_info = cursor.fetchall()
            user_info = [
                {
                    'name' : u[0],
                    'email' : u[1],
                    'address' : u[2],
                    'phone' : u[3]
                } for u in user_info
            ]

            # return redirect(url_for('bp.payment', user_id=user_id, sum_total=sum_total))
            return render_template('orders.html', payments=payments, sum_total=sum_total, item_count=item_count, user_info=user_info, user_id=user_id)

        except:
            None
            # return("오류"), 401
          
        
@bp.route('/<int:user_id>/payment', methods=('GET', 'POST'))
def payment(user_id):
    if request.method == 'GET':
       
        return("GET"), 200
        
    elif request.method == 'POST':

        cursor.execute("SELECT user_id, u.wallet_id, w.rest from wallet as w join users as u where user_id='{}';".format(user_id))
        wallet = cursor.fetchone()

        user_id = wallet[0]
        wallet_id = wallet[1]
        rest = int(float(wallet[2]))

        sum_total = int(float(request.form['sum_total']))


            # 총 금액과 지갑 비교
        if sum_total <= rest:
            afterest = rest - sum_total
            cursor.execute("update wallet set rest='{}' where wallet_id = {};".format(afterest, wallet_id))
            db.commit()
            flash('결제가 완료되었습니다!')
            return render_template('orders.html', user_id=user_id), 200
        else:
            flash('잔액이 부족합니다.')
            return render_template('orders.html', user_id=user_id), 200

        

