import pymysql
import re

from flask import Blueprint, render_template, request, redirect
from my_settings import PW

bp = Blueprint('signup', __name__, url_prefix='/users')

# 데이터베이스 접근
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
        if request.method == 'POST':
            if 'email_check' in request.form: # 중복확인 버튼을 눌렀을 때
                email = request.form['email']
                cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
                user = cursor.fetchone()
                if user:
                    msg = '이미 등록된 이메일입니다.'
                else:
                    msg = '사용 가능한 이메일입니다.'
            
            else: 
                name = request.form['name']
                email = request.form['email']
                domain = request.form['domain']
                password = request.form['password']
                address = request.form['address']
                phone = request.form['phone']
                wallet_id = 0
        
        # 이미 존재하는 계정인지 확인
                cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
                user = cursor.fetchone()
                cursor.execute('SELECT MAX(wallet_id) FROM users')
                max_wallet_id = cursor.fetchone()[0]
                wallet_id = max_wallet_id + 1 if max_wallet_id is not None else 1
        
                cursor.execute('INSERT INTO users (name, email, password, address, phone, wallet_id) VALUES \
                (%s, %s, %s, %s, %s, %s)', (name, email+domain, password, address, phone, wallet_id))
                db.commit()
                msg = '가입을 환영합니다!'
                return render_template('signin.html')

        else:
            msg = 'Please fill out the form!'
            return render_template('signup.html', msg=msg)

@bp.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    user = cursor.fetchone()
    if user:
        result = {'result': 'fail'}
    else:
        result = {'result': 'success'}
    return result
