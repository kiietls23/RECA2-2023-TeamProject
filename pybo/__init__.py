from flask import Flask



def create_app():
    app = Flask(__name__)
<<<<<<< HEAD
    app.secret_key = 'abab'
    # 블루프린트
    from .views import login, cart, product, orders, signup

    
=======
    app.secret_key = 'your_secret_key_here'

    # 블루프린트
    from .views import main_views, login, mypage, cart, product, orders, main

    app.register_blueprint(main_views.bp)
    app.register_blueprint(main.bp)
>>>>>>> 88058fefc1f5c08134a65761086b5c3d15c43a53
    app.register_blueprint(login.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(orders.bp)

    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
    

   
    app.secret_key = '1234'


    return app
