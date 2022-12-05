import json


def get_posts_all() -> list[dict]:
    """
    Возвращает посты
    """
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(username: str) -> list[dict]:
    """
    Возвращает посты определенного пользователя.
    """
    result = []
    for post in get_posts_all():
        if username.lower() in post['poster_name'].lower():
            result.append(post)
    return result


def get_comments_by_post_id(post_id: int) -> list[dict]:
    """
    Возвращает комментарии определенного поста.
    """
    result = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        post_comments = json.load(file)
    for comment in post_comments:
        if post_id == comment['post_id']:
            result.append(comment)
    return result


def count_comments(post_id: int):
    comments = 0
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        post_comments = json.load(file)
    for comment in post_comments:
        if post_id == comment['post_id']:
            comments += 1
    return comments


def search_for_posts(query: str) -> list[dict]:
    """
    Возвращает список постов по ключевому слову.
    """
    result = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result


def count_posts(query: str):
    count = 0
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            count += 1
    return count


def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору.
    """
    for post in get_posts_all():
        if pk == post['pk']:
            return post
    return f"Пост не найден"