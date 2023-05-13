import pymysql
import re

from flask import Blueprint, render_template, request, session, Flask, url_for, redirect, flash

from my_settings import PW



bp = Blueprint('login', __name__, url_prefix='/users' )

db = pymysql.connect(host='localhost',            # database 접근
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')


cursor = db.cursor()                               # database 테이블에 접근  



@bp.route('/signin')
def login_page():
    return render_template('/signin.html')

@bp.route('/signin', methods=['GET', 'POST'])
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
            flash("이메일 또는 비밀번호가 올바르지 않습니다.")
            return render_template ('signin.html')
    else:
        return render_template ('signin.html')
    
@bp.route('/signup')
def sign_up_page():
    return render_template('signup.html')

@bp.route('/log_out')
def logout():
    session.pop('email')
    session.pop('password')
    session.pop('name')
    session.clear()
    return redirect(url_for('main.main'))