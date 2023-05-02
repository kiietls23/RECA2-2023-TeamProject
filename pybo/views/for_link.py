from flask import Blueprint, render_template, Flask, url_for,redirect

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def main_logoff():
    return render_template('/index_before_login.html')  

@bp.route('/login_page')
def login_page():
    return render_template('/signin.html')

@bp.route('/login')
def main_login():
    return render_template('/index_after_login.html')