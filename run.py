from flask import Flask

from api import api_bp
from views import main_bp

POST_PATH = 'data/posts.json'
UPLOAD_FOLDER = 'uploads/images'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(api_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000)
