from flask import Flask
from config import Config
from app.extension import *

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Inisialisasi ekstensi flask
    db.init_app(app)

    #Mendaftarkan alamat blueprint
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.upload import bp as upload_bp
    app.register_blueprint(upload_bp, url_prefix='/upload')
    
    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

        
    @app.route('/test/')
    def test_page():
        return '<p>This is test page</p>'
    return app

if __name__ == '__main__':
    app = create_app
    app.run()