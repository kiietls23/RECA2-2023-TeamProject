from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루프린트
    from .views import catalog, for_link, login, mypage

    app.register_blueprint(for_link.bp)
    app.register_blueprint(catalog.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(mypage.bp)

    return app