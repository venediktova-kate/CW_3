import logging

import utils
from flask import Flask, request, render_template

from api.api import api_bp

app = Flask(__name__)

app.register_Blueprint(api_bp)


@app.route('/')
def main_page():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def post_page(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    count_comments = utils.count_comments(post_id)
    return render_template('post.html', post=post, comments=comments, count=count_comments)


@app.route('/search/')
def search_page():
    search_query = request.args.get('s', '')
    logging.info('Выполняю поиск')
    count_posts = utils.count_posts(search_query)
    posts = utils.search_for_posts(search_query)
    return render_template('search.html', query=search_query, posts=posts, count=count_posts)


@app.route('/users/<username>')
def users_page(username: str):
    user_posts = utils.get_posts_by_user(username)
    print(user_posts)
    return render_template('user-feed.html', posts=user_posts)


app.run()
