import pymysql

from flask import Blueprint, render_template, request, redirect, url_for

from my_settings import PW

#블루프린트
bp = Blueprint('cart', __name__, url_prefix='/cart')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()


    
@bp.route('/<int:user_id>', methods=['GET', 'POST'])
def get(user_id):
    #장바구니 조회
    if request.method == 'GET':
        try:
            db.commit()
            cursor.execute("""select c.cart_id, p.name, p.price, p.delivery_charge, c.count 
                        from cart as c join products as p
                        on c.product_id = p.product_id 
                        where c.user_id={}
                        """.format(user_id))
            carts = cursor.fetchall()
            if len(carts) == 0:
                return("장바구니가 비어있음"), 200
            results = [
                {
                    'cart_id': cart[0],
                    'name': cart[1],
                    'price': int(cart[2]),
                    'delivery_charge': int(cart[3]),
                    'count' : int(cart[4]),
                    'total_price' : int((cart[2]*cart[4])+cart[3])
                } for cart in carts
            ]
            # return(results), 200
            return render_template('cart.html', results=results, user_id=user_id), 200
        except:
            return("장바구니 조회 오류"), 401
        
    # 장바구니 테이블 -> 결제 테이블
    elif request.method == 'POST':
        try:
                       
            cursor.execute("select c.user_id, p.product_id, p.name, p.price, c.count from cart as c join products as p on c.product_id = p.product_id where user_id = '{}';".format(user_id))
            payments = cursor.fetchall()

            results = [
                {
                    'user_id' : payment[0],
                    'product_id' : payment[1],
                    'name' : payment[2],
                    'price' : payment[3],
                    'count' : payment[4],
                    'sum' : int(payment[3]) * int(payment[4]),
                } for payment in payments
            ]
               
            for payment in payments:
                user_id = payment[0]
                product_id = payment[1]
                count = payment[4]

                data = {
                    'user_id' : user_id,
                    'product_id' : product_id,
                    'count' : count
                }
                columns = ', '.join(data.keys())
                values = ', '.join(['%s']*len(data))


                query = 'insert into payments (%s) values (%s);' % (columns, values)
                cursor.execute(query, tuple(data.values()))

            db.commit()

            return(results), 200
            
        except:
            None
            # return({'message':'실패'})

        
@bp.route('/edit', methods=['POST'])
#장바구니 수정/삭제
def edit():
    if request.form['action'] == '수정':
        try:
            cart_id = request.form["cart_id"]
            user_id = request.form["user_id"]
            count = request.form["count"]

            sql = "update shop.cart set count={} where cart_id={}".format(count, cart_id)

            cursor.execute(sql)
            db.commit()
            return redirect(url_for('cart.get', user_id=user_id))
        except:
            return("오류"), 401
    elif request.form['action'] == '삭제':
        try:
            cart_id = request.form["cart_id"]
            user_id = request.form["user_id"]

            sql = "delete from cart where cart_id={}".format(cart_id)

            cursor.execute(sql)
            db.commit()
            return redirect(url_for('cart.get', user_id=user_id))
        except:
            return("오류"), 401