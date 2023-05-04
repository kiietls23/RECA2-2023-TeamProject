from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'

    # 블루프린트
    from .views import main_views, catalog, for_link, login, mypage, cart, product, orders

    app.register_blueprint(main_views.bp)
    app.register_blueprint(for_link.bp)
    app.register_blueprint(catalog.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(mypage.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(orders.bp)

    app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
    

    return app
