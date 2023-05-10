from flask import Blueprint, render_template, Flask, url_for, redirect,request, session
import pymysql
import random
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
    nn = random.sample(range(0, 18), 6)
    product_ids = [str(n) for n in nn]  # convert product_ids to strings

    query = "SELECT description, SUBSTRING_INDEX(name, ' ', 1), product_id FROM products WHERE product_id IN ({}, {}, {}, {}, {}, {})".format(*product_ids)
    cursor.execute(query)
    results = cursor.fetchall()

    data_list = [{'description': row[0], 'titles': row[1], 'product_id': str(row[2])} for row in results]
    data = pd.DataFrame(data_list)
    data_list = zip(data['description'], data['titles'], data['product_id'])

    return render_template('/index_before_login.html', data=data_list)