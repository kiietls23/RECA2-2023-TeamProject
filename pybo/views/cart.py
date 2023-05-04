import pymysql

from flask import Blueprint, render_template, request

from my_settings import PW

#블루프린트
bp = Blueprint('cart', __name__, url_prefix='/cart')

#db
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()


    
@bp.route('/<int:user_id>')
#장바구니 조회
def get(user_id):
    try:
        cursor.execute("""select p.name, p.price, p.delivery_charge, c.count 
                       from cart as c join products as p
                       on c.product_id = p.product_id 
                       where c.user_id={}
                       """.format(user_id))
        carts = cursor.fetchall()
        if len(carts) == 0:
            return("장바구니가 비어있음"), 200
        results = [
            {
                'name': cart[0],
                'price': int(cart[1]),
                'delivery_charge': int(cart[2]),
                'count' : int(cart[3]),
                'total_price' : int((cart[1]*cart[3])+cart[2])
            } for cart in carts
        ]
        return(results), 200
    except:
        return("오류"), 401