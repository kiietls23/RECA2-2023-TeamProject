from flask import Blueprint, render_template, Flask, url_for, redirect,request
import pymysql
import pandas as pd
bp = Blueprint('catalog',__name__,url_prefix='')
db = pymysql.connect(host='localhost',            # database 접근
                    user='root',
                    password='',
                    db='shop',
                    charset='utf8mb4')
cursor = db.cursor() 

@bp.route('tops_page_logoff')
def top_page_logoff():
    cursor.execute("select * from products where tag='티셔츠'")
    item_url = cursor.fetchall()
    cursor.execute("SELECT SUBSTRING_INDEX(name, ' ', 1) from products")
    item_title = cursor.fetchall()

    data_list = [{'images': a[2], 'titles': b[0]} for a, b in zip(item_url, item_title)]
    data = pd.DataFrame(data_list)

    data_list = zip(data['images'], data['titles'])
    
    return render_template('/top_page_logoff.html', data=data_list) 

@bp.route('/tops_page_logon')
def top_page_logon():
    return render_template('/top_page_logon') 





@bp.route('/bottom_page_logoff')
def bottom_page_logoff():
    return render_template('/bottom_page_logoff.html')


@bp.route('/bottom_page_logon')
def bottom_page_logon():
    return render_template('/bottom_page_logon.html')





@bp.route('/shoes_page_logoff')
def shoes_page_logoff():
    return render_template('/shoes_page_logoff.html.html')

@bp.route('/shoes_page_logon')
def shoes_page_logon():
    return render_template('/index_after_login.html.html')

