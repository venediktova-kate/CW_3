from flask import Flask

from config import Config
from app import create_app

app: Flask = create_app(Config)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000)
