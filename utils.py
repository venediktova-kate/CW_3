import json


def get_posts_all() -> list[dict]:
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)
#возвращает посты


def get_posts_by_user(user_name: str) -> list[dict]:
    result = []
    for post in get_posts_all():
        if user_name.lower() in post['poster_name'].lower():
            result.append(post)
    return result
#возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов.


def get_comments_by_post_id(post_id: int) -> list[dict]:
    result = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        post_comments = json.load(file)
    for comment in post_comments:
        if post_id == comment['post_id']:
            result.append(comment)
    return result
#возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов.


def count_comments(post_id: int):
    comments = 0
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        post_comments = json.load(file)
    for comment in post_comments:
        if post_id == comment['post_id']:
            comments += 1
    return comments


def search_for_posts(query: str) -> list[dict]:
    result = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result
#возвращает список постов по ключевому слову


def count_posts(query: str):
    count = 0
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            count += 1
    return count


def get_post_by_pk(pk) -> dict:
    for post in get_posts_all():
        if pk == post['pk']:
            return post
#возвращает один пост по его идентификатору.