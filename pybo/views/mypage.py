
from flask import Blueprint, render_template, Flask, url_for, redirect, request, g, session

import pymysql
from my_settings import PW

bp = Blueprint('mypage',__name__,url_prefix='/user')

db = pymysql.connect(host='127.0.0.1',            # database 접근
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')


cursor = db.cursor()                               # database 테이블에 접근  



## 개인정보 확인

@bp.route('/info')
def info_page():
    if session:
        email = session['email']
        password = session['password']
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        selectrow = cursor.fetchall()  ## 모든 raw를 선택한 것을 allraw로 정의
        if selectrow:
            results = [{                                      ## results에 데이터베이스에서 불러올 값 넣어주기
            'name' : a[1],                              
            'created_at' : a[6],                              
            'id' : a[0],                       
            'phone' : a[5],                            
            'email' : a[2],
            'address' : a[4],                               
            }  for a in selectrow ]                                  
            return render_template('user_info.html',results=results)
        else:
            return redirect(url_for('login.login'))
        
    else:
        return redirect(url_for('login.login'))

## 개인정보 변경

@bp.route('/info_change',methods=['POST'])
def info_change():
    if request.method == 'POST':
        id = request.form["user_id"]
        after_phone = request.form['phone']
        after_email = request.form['email']
        session['email'] = request.form['email']
        after_address = request.form['address']
        cursor.execute("UPDATE users SET phone = %s, email = %s, address = %s WHERE user_id = %s", (after_phone, after_email, after_address, id,))
        db.commit()
        return redirect(url_for('mypage.info_page'))
    else:
        pw = None
    return redirect('/info')






## 비밀번호 페이지

@bp.route('/pw_change')
def pw_page():
    if session:
        email = session['email']
        password = session['password']
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        selectrow = cursor.fetchall() 
        if selectrow:
            return render_template('user_pw_change.html')
        else:
            return redirect(url_for('login.login'))
    else:
        return redirect(url_for('login.login'))
## 비밀번호 변경

@bp.route('/password_change',methods=['POST'])
def pw_change():
    if request.method == 'POST':
        email = session['email']
        pw = request.form['pw']
        session['password'] = pw
        cursor.execute("UPDATE users SET password = %s WHERE email= %s ",(pw, email))
        db.commit()
    else:
        pw = None
    return redirect('/user/pw_change')


## 탈퇴 페이지

@bp.route('/del')
def del_page():
    if session:
        email = session['email']
        password = session['password']
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s', (email, password))
        selectrow = cursor.fetchall() 
        if selectrow:
            return render_template('user_delete.html')
        else:
            return redirect(url_for('login.login'))
    else:
        return redirect(url_for('login.login'))
    


@bp.route('/delete',methods=['POST'])
def delete():
        
    if request.method == 'POST':
        email = session['email']
        cursor.execute('DELETE FROM users WHERE email = %s', (email,))
        cursor.execute("SET @num := 0")
        cursor.execute("UPDATE users SET user_id = @num := @num + 1" )
        db.commit()
        return redirect(url_for('login.logout'))
    else:
        user_id = None
        return redirect(url_for('del_page'))

