from flask import Flask
from pages.back.controllers.list_controller import list_bp
from pages.back.controllers.task_controller import task_bp

app = Flask(__name__)
app.register_blueprint(list_bp)
app.register_blueprint(task_bp, url_prefix="/task")
# secret_key required for flash to work properly
app.secret_key = "key_secret"

if __name__ == '__main__':
    app.run(debug=True)
