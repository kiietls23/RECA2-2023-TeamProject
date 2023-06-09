import pymysql

from flask import Blueprint, render_template, request, redirect, url_for, session

from my_settings import PW

#블루프린트
bp = Blueprint('cart', __name__, url_prefix='/cart')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()

@bp.route('/')
def cart_check():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login.login'))
    else:
        return redirect(url_for('cart.get',user_id=session['user_id']))

@bp.route('/<int:user_id>', methods=['GET'])
def get(user_id):
    #장바구니 조회
    try:
        db.commit()
        cursor.execute("""select c.cart_id, p.name, p.price, p.delivery_charge, c.count, p.description, p.product_id
                    from cart as c join products as p
                    on c.product_id = p.product_id 
                    where c.user_id={}
                    """.format(user_id))
        carts = cursor.fetchall()
        if len(carts) == 0:
            return """<script>alert('장바구니가 비어있습니다. 메인 페이지로 돌아갑니다.');
        window.location.replace('http://127.0.0.1:5000/main');</script>"""

        results = [
            {   
                'product_id' : cart[6],
                'description' : cart[5],
                'cart_id': cart[0],
                'name': cart[1],
                'price': int(cart[2]),
                'delivery_charge': int(cart[3]),
                'count' : int(cart[4]),
                'total_price' : int((cart[2]*cart[4])+cart[3])
            } for cart in carts
        ]
        return render_template('cart.html', results=results, user_id=user_id), 200
    except:
        return("장바구니 조회 오류"), 401

        
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