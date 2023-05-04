import pymysql

from flask import Blueprint, render_template, request

from my_settings import PW


bp = Blueprint('main', __name__, url_prefix='/koko')

# database 접근
db = pymysql.connect(host='127.0.0.1', user='root', password=PW, db='shop', charset='utf8')
# database 테이블에 접근
cursor = db.cursor()

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST' \
	and 'name' in request.form \
	and 'email' in request.form \
    and 'password' in request.form \
    and 'address' in request.form \
	and 'phone' in request.form:
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']
		address = request.form['address']
		phone = request.form['phone']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute(
			'SELECT * FROM user WHERE account = % s', (account, ))
		user = cursor.fetchone()
		if user:
			msg = '이미 존재하는 계정입니다 !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = '이메일 형식에 맞지 않습니다 !'
		elif not re.match(r'^[a-zA-Z0-9가-힣]+$', username):
			msg = '이름은 영어와 숫자, 한글로만 구성되어야 한다 !'
		else:
			cursor.execute('INSERT INTO user VALUES \
		        (% s, % s, % s, % s, % s, % s, % s)', 
               (account, password, username, email, gender, birth, phonenumber))
			mysql.connection.commit()
			msg = '가입을 환영합니다 !'
			return redirect('/login')
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('signup.html', msg=msg)