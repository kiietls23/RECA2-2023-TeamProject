import pymysql

from flask import Blueprint, render_template, request, session, Flask, url_for, redirect

from my_settings import PW

from flask import Flask, session


bp = Blueprint('login', __name__, url_prefix='/' )

db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')

cursor = db.cursor()

        
@bp.route('/login', methods=['GET', 'POST'])
def home():
    return render_template('signin.html')

@bp.route('/login_process', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute('SELECT email, password FROM users WHERE email = %s AND password = %s;', (email, password))
        user = cursor.fetchone()
        if user is not None:
            session['email'] = user[0]
            session['password'] = user[1]
            return render_template('signup.html')
        else:
            return render_template('signin.html', error="이메일 또는 비밀번호가 올바르지 않습니다.")
    else:
        return redirect ('signup.html')

