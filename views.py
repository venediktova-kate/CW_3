from flask import Blueprint, render_template, request
import logging
import utils

main_bp = Blueprint('views', __name__)


@main_bp.route('/')
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@main_bp.route('/posts/<int:post_id>')
def post_page(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    count_comments = utils.count_comments(post_id)
    return render_template('post.html', post=post, comments=comments, count=count_comments)


@main_bp.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    count_posts = utils.count_posts(search_query)
    posts = utils.search_for_posts(search_query)
    return render_template('search.html', query=search_query, posts=posts, count=count_posts)


@main_bp.route('/users/<string:username>', methods=['GET'])
def users_page(username):
    user_posts = utils.get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, username=username)
