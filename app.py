from flask import Flask

from api.api import api_bp
from main.views import main_bp

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api_bp)
app.register_blueprint(main_bp)


if __name__ == '__main__':
    app.run(debug=True)
