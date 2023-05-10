
from flask import Blueprint, render_template, Flask, url_for, redirect, request, g, session

import pymysql
from my_settings import PW

bp = Blueprint('search',__name__,url_prefix='/search')

db = pymysql.connect(host='127.0.0.1',            # database 접근
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')


cursor = db.cursor()                               # database 테이블에 접근  



## 개인정보 확인

@bp.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword'] # 검색어 가져오기
        cursor.execute("SELECT description, name, tag, price, product_id FROM products WHERE name LIKE '%{}%'".format(keyword))
        answer = cursor.fetchall()
        if answer:
            results = [{
                'image': i[0],
                'name': i[1],
                'tag': i[2],
                'price': i[3],
                'product_id':i[4]
            } for i in answer]
            return render_template('search.html', results=results)
        else:
            return render_template('search.html')
    else:
        return render_template('search.html')







        