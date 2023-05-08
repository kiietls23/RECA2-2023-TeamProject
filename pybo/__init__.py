from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'abab'
    # 블루프린트
    from .views import login, cart, product, orders, signup

    
    app.register_blueprint(login.bp)
    app.register_blueprint(signup.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(orders.bp)

    return app