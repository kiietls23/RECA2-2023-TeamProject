
from flask import Blueprint, render_template, Flask, url_for, redirect, request, g

import pymysql

bp = Blueprint('mypage',__name__,url_prefix='/mypage')

db = pymysql.connect(host='127.0.0.1',            # database 접근
                    user='root',
                    password='',
                    db='shop',
                    charset='utf8mb4')


cursor = db.cursor()                               # database 테이블에 접근  



## 개인정보 확인

@bp.route('/info_check')
def info_check():
    cursor.execute("select * from users WHERE name = '박하하'")        ## users라는 table의 모든 column을 선택
    selectrow = cursor.fetchall()  ## 모든 raw를 선택한 것을 allraw로 정의
    results = [

        {                                      ## results에 데이터베이스에서 불러올 값 넣어주기
            'name' : a[1],                              
            'created_at' : a[6],                              
            'id' : a[0],                       
            'phone' : a[5],                            
            'email' : a[2],
            'address' : a[4],                               
            }  for a in selectrow
            
    ]       
    db.commit()                                          
    return render_template('check_after_login.html',results=results)

## 개인정보 변경

@bp.route('/info_change',methods=['POST'])
def info_change():
    if request.method == 'POST':
        id = request.form["user_id"]
        after_phone = request.form['phone']
        after_email = request.form['email']
        after_address = request.form['address']
        cursor.execute("UPDATE users SET phone = %s, email = %s, address = %s WHERE user_id = %s", (after_phone, after_email, after_address, id,))
        
    else:
        pw = None
    return redirect ('info_check')






## 비밀번호 페이지

@bp.route('/pw_change')
def pw_change():
    return render_template('change_after_login.html')

## 비밀번호 변경

@bp.route('/change_password',methods=['POST'])
def change_password():
    if request.method == 'POST':
        pw = request.form['pw']
        cursor.execute("UPDATE users SET password = %s WHERE user_id= 0 ",(pw,))
        db.commit()
    else:
        pw = None
    return redirect( 'pw_change')


## 탈퇴 페이지

@bp.route('/del_user')
def del_user():
    cursor.execute("SELECT * FROM users WHERE user_id='0' ")          
    selectraw = cursor.fetchall()  
    results = [
        {                                      
            'name' : a[1],                              
            'created_at' : a[6],                              
            'id' : a[0],                       
            'phone' : a[5],                            
            'email' : a[2],
            'address' : a[4],                               
            }  for a in selectraw                          
    ]                       
    
                        
    return render_template('delete_after_login.html',results=results)


@bp.route('/delete',methods=['POST'])
def delete():
    if request.method == 'POST':
        cursor.execute("DELETE FROM users WHERE user_id = '0' ")
    else:
        user_id = None
    db.commit()
    return redirect('del_user')

