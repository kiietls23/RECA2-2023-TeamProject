from flask import Flask



def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'

    # 블루프린트
    from .views import main_views, login, mypage, cart, product, orders, main, signup

    app.register_blueprint(main_views.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(mypage.bp)

    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
    


    app.secret_key = '1234'


    return app
from flask import Flask



def create_app():
    app = Flask(__name__)
    app.secret_key = '1234'

    # 블루프린트
    from .views import main_views, login, mypage, cart, product, orders, main, signup

    app.register_blueprint(main_views.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(mypage.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(signup.bp)

    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])


    return app
