import pymysql
from flask import Blueprint, render_template, request, url_for, redirect, session
from my_settings import PW

#블루프린트
bp = Blueprint('orders', __name__, url_prefix='/orders')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()

@bp.route('/<int:user_id>', methods=('GET', 'POST'))
# 장바구니에서 가져온 결제 정보 조회(payments, products 테이블)
def get(user_id):
    if request.method == 'GET':
        try:
            db.commit()
            cursor.execute("""select p.product_id, p.name, p.price, p.delivery_charge, c.count
                            from cart as c join products as p
                            on c.product_id = p.product_id 
                            where c.user_id={}
                            """.format(user_id))
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
                item_count += p['count']
            
            session['test'] = sum_total

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
            
            return render_template('orders.html', payments=payments, sum_total=sum_total, item_count=item_count, user_info=user_info, user_id=user_id)

        except:
            None
            # return("오류"), 401
        
        
@bp.route('/<int:user_id>/payment', methods=('GET', 'POST'))
def payment(user_id):
    if request.method == 'GET':
    
        return("GET"), 200
        
    elif request.method == 'POST':
        cursor.execute("""select u.user_id, u.wallet_id, w.rest 
                        from wallet as w join users as u 
                        on u.wallet_id = w.wallet_id 
                        where u.user_id={}""".format(user_id))
        wallet = cursor.fetchone()
        

        user_id = wallet[0]
        wallet_id = wallet[1]
        rest = int(float(wallet[2]))

        sum_total = session.get('test')

            # 총 금액과 지갑 비교
        if int(sum_total) <= rest:
            afterest = rest - sum_total
            cursor.execute("update wallet set rest='{}' where wallet_id = {};".format(afterest, wallet_id))
            db.commit()
            # 주문 내역 페이지로 이동 (현재는 우선 mypage로 이동)
            return '''<script>alert('결제가 완료되었습니다!');
                    window.location.href = '{0}';</script>'''.format(url_for('mypage.info_page', user_id=user_id))
        else:
            return '''<script>alert('잔액이 부족합니다. 지갑을 충전하세요!');
                    window.location.href = '{0}';</script>'''.format(url_for('mypage.info_page', user_id=user_id))


@bp.route('/<product_id>/<count>')
# 상품페이지에서 가져온 결제 정보 조회(payments, products 테이블)
def getproduct(product_id, count):
    try:
        user_id = session.get('user_id')
        product_id = int(product_id)
        count = int(count)

        cursor.execute("""select product_id, name, price, delivery_charge
                        from products
                        where product_id={}
                        """.format(product_id))
        products = cursor.fetchall()

        payments = [
            {
                'product_id': product[0],
                'count' : count,
                'name': product[1],
                'price': int(product[2]),
                'delivery_charge': int(product[3]),
                'total_price' : int((product[2]*count)+product[3])
            } for product in products
        ]

        item_count = 0
        sum_total = 0

        # 총 합계 금액 sum_total과 결제할 상품 개수 item_count 계산
        for p in payments:
            sum_total += p['total_price']
            item_count += p['count']

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

        return render_template('orders.html', payments=payments, sum_total=sum_total, item_count=item_count, user_info=user_info, user_id=user_id)

    except:
        None
        # return("오류"), 401