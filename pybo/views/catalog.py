from flask import Blueprint, render_template, Flask, url_for, redirect, request, session, jsonify
import pymysql
import pandas as pd
from my_settings import PW
bp = Blueprint('catalog',__name__,url_prefix='/products')
db = pymysql.connect(host='localhost',            # database 접근
                    user='root',
                    password=PW,
                    db='shop',
                    charset='utf8mb4')
cursor = db.cursor() 
@bp.route('/')
def catalogy():
    abc = request.args.get('value')
    return render_template('index.html',abc=abc)


@bp.route('/<string:abc>')
def catalog(abc):
    current_url = request.url
    if abc == "TOPS":
        it = '티셔츠'
    elif abc == "BOTTOMS":
        it = '하의'
    else:
        it = '신발'
        
    cursor.execute("select * from products where tag= %s",(it))
    item_url = cursor.fetchall()
    cursor.execute("SELECT SUBSTRING_INDEX(name, ' ', 1) from products where tag= %s",(it))
    item_title = cursor.fetchall()
    cursor.execute("select product_id from products where tag= %s",(it))
    item_number = cursor.fetchall()
    data_list = [{'images': a[2], 'titles': b[0], 'items':c[0]} for a, b, c in zip(item_url, item_title, item_number)]
    data = pd.DataFrame(data_list)

    data_list = zip(data['images'], data['titles'], data['items'])

    return render_template('/category.html', data=data_list, abc=abc)












