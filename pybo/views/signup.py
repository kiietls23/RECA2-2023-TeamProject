import pymysql
import re

from flask import Blueprint, render_template, request, redirect
from my_settings import PW

bp = Blueprint('signup', __name__, url_prefix='/users')

# 데이터베이스 접근
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
cursor = db.cursor()


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

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if 'email_check' in request.form: # When the duplicate check button is clicked
            email = request.form['email']
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cursor. fetchone()
            if user:
                msg = 'This email is already registered.'
            else:
                msg = 'Your email is available.'
            return render_template('signup.html', msg=msg)
        else:
            name = request.form['name']
            email = request.form['email']
            domain = request.form['domain']
            password = request.form['password']
            address = request.form['address']
            phone = request.form['phone']
            wallet_id = 0
            
            # Check if the account already exists
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cursor. fetchone()
            if user:
                msg = 'This email is already registered.'
                return render_template('signup.html', msg=msg)
            
            # Check if all fields are filled
            if not name or not email or not domain or not password or not address or not phone:
                msg = 'Please fill out all fields!'
                return render_template('signup.html', msg=msg)
                
            cursor.execute('SELECT MAX(wallet_id) FROM users')
            max_wallet_id = cursor.fetchone()[0]
            wallet_id = max_wallet_id + 1 if max_wallet_id is not None else 1
            
            cursor.execute('INSERT INTO users (name, email, password, address, phone, wallet_id) VALUES \
            (%s, %s, %s, %s, %s, %s)', (name, email+"@"+domain, password, address, phone, wallet_id))
            db.commit()
            msg = 'Welcome to join!'
            return render_template('signin.html')
    else:
        msg = 'Please fill out the form!'
    return render_template('signup.html', msg=msg)

