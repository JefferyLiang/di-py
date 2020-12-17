def create_app():
    from flask import Flask
    import os
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello'

    from lib.di import DI
    di = DI(app, os.path.abspath(f'{os.environ.get("FLASK_APP")}'))
    di.scan_modules(['models'])
    di.import_modules()

    return app
