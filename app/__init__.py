from flask import Flask, render_template, Blueprint
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

    @app.route('/test/')
    def test_page():
        return '<p>This is test page</p>'
    return app