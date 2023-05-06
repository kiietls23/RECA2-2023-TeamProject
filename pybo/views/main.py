from flask import Blueprint, render_template, Flask, url_for,redirect
from flask import Blueprint, render_template, Flask, url_for, redirect,request
import pymysql
import pandas as pd
from my_settings import PW

bp = Blueprint('main',__name__,url_prefix='/main')
db = pymysql.connect(host='localhost',
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')

cursor = db.cursor() 

@bp.route('/')
def main():
    cursor.execute("select * from products order by rand() limit 6")
    item_url = cursor.fetchall()
    

    cursor.execute("SELECT SUBSTRING_INDEX(name, ' ', 1) from products")
    item_title = cursor.fetchall()

    data_list = [{'images': a[2], 'titles': b[0]} for a, b in zip(item_url, item_title)]
    data = pd.DataFrame(data_list)

    data_list = zip(data['images'], data['titles'])
    
    return render_template('/index_before_login.html', data=data_list) 



