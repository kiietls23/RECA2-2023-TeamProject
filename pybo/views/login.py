import pymysql

from flask import Blueprint, render_template, request, session, Flask, url_for, redirect

from my_settings import PW



bp = Blueprint('login', __name__, url_prefix='/user' )

db = pymysql.connect(host='localhost',            # database 접근
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')


cursor = db.cursor()                               # database 테이블에 접근  



@bp.route('/sign_in')
def login_page():
    return render_template('/signin.html')

@bp.route('/sign_in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        user = cursor.fetchone()

        if user is not None:
            session['email'] = user[2]
            session['password'] = user[3]
            session['name']=user[1]
            session['user_id']=user[0]
            
            return redirect(url_for('main.main'))
        else:
            return "이메일 또는 비밀번호가 올바르지 않습니다."
    else:
        return render_template ('signin.html')
    
@bp.route('/sign_up')
def sign_up_page():
    return render_template('sign_up-2.html')

@bp.route('/log_out')
def logout():
    session.pop('email')
    session.pop('password')
    session.pop('name')
    session.clear()
    return redirect(url_for('main.main'))
