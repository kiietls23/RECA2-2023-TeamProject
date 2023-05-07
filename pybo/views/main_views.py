import pymysql

from flask import Blueprint, render_template

from my_settings import PW


bp = Blueprint('vss', __name__, url_prefix='/koko')

# database 접근
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
# database 테이블에 접근
cursor = db.cursor()



@bp.route('/')
def index():
    cursor.execute("select * from users")
    users = cursor.fetchall()
    results = [
        {
            'user_id' : user[0],
            'name' : user[1],
            'email' : user[2],
            'address' : user[4],
            'phone' : user[5],
        } for user in users
    ]
    return render_template('user.html', results=results), 200
    # return(results)
    





    
