from flask import Flask
from pages.back.controllers.list_controller import list_bp

app = Flask(__name__)
app.register_blueprint(list_bp, url_prefix="/list")


if __name__ == '__main__':
    app.run(debug=True)
