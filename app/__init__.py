from flask import Flask

from config import Config
from app.extension import *

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Inisialisasi ekstensi flask
    db.init_app(app)
    #login_manager.init_app(app)

    #Mendaftarkan alamat blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.penjualan import bp as penjualan_bp
    app.register_blueprint(penjualan_bp, url_prefix='/penjualan')
    
    from app.peramalan import bp as peramalan_bp
    app.register_blueprint(peramalan_bp, url_prefix='/peramalan')

        
    @app.route('/test/')
    def test_page():
        return '<p>This is test page</p>'
    return app

    if __name__ == '__main__':
        app.run()
'''
from app.model.user import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
'''