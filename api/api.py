from flask import Blueprint, jsonify

import utils
import logging

api_bp = Blueprint('api', __name__, url_prefix='/api/')
logging.basicConfig(filename="api.log", level=logging.INFO)


@api_bp.route('post/')
def main_page():
    logging.info("Страница /api/posts запрошена")
    posts = utils.get_posts_all()
    return jsonify(posts)


@api_bp.route('posts/<int:post_id>')
def post_page(post_id):
    logging.info(f"Страница /api/posts/{post_id} запрошена")
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    return jsonify(post)