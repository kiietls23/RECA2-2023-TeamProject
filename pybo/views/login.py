
import pymysql
from flask import Blueprint, render_template, request, session, Flask, url_for, redirect
from my_settings import PW



bp = Blueprint('login', __name__, url_prefix='/login_page' )

db = pymysql.connect(host='localhost',            # database 접근
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')


cursor = db.cursor()                               # database 테이블에 접근  




@bp.route('/')
def home():
    user = session.get('user')
    if user is not None:
        email = user['email']
        password = user['password']
        return render_template('/user.html')
    else:
        return render_template('/user.html')

@bp.route('/login', methods=['POST'])
def login():
    print ("hello world")
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT email, password FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()
        if user is not None:
            session['email'] = user[0]
            session['password'] = user[1]
            return render_template('/index_after_login.html')
        else:
            return render_template('/user.html', error="이메일 또는 비밀번호가 올바르지 않습니다.")
    else:
        return render_template('/user.html')

@bp.route('/login_page/sign_up_page')
def sign_up_page():
    return render_template('sign_up-2.html')