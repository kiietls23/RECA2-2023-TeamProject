from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루프린트
    from .views import main_views, cart, product
    app.register_blueprint(main_views.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(product.bp)
    

    return app