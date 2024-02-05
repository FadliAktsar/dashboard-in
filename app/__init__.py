from flask import Flask, Blueprint

from config import Config
from app.extension import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Inisialisasi ekstensi flask
    db.init_app(app)

    #Mendaftarkan alamt blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')
    
    from app.register import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/register')

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