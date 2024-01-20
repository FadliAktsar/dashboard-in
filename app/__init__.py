from flask import Flask, render_template, Blueprint
from flask_bootstrap import Bootstrap
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Initialize Flask Extension

    #Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.login import bp as login_bp
    app.register_blueprint(login_bp)

    from app.penjualan import bp as penjualan_bp
    app.register_blueprint(penjualan_bp)
    
    from app.peramalan import bp as peramalan_bp
    app.register_blueprint(peramalan_bp)

        
    @app.route('/test/')
    def test_page():
        return '<p>This is test page</p>'
    return app

    if __name__ == '__main__':
        Bootstrap(app)
        app.run()