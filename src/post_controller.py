import requests


def get_posts(limit: int = 0):
    response = requests.get(
        f"https://dummyjson.com/posts",
        params={"limit": limit},
    )

    return response.json()


def search_posts(query: str, limit: int = 0):
    response = requests.get(
        f"https://dummyjson.com/posts/search",
        params={"limit": limit, "q": query},
    )

    return response.json()


def get_post_by_tag(tag: str):
    response = requests.get(f"https://dummyjson.com/posts/tag/{tag}")
    return response.json()


def create_post(user_id: int, id: int, title: str):
    response = requests.post(
        "https://dummyjson.com/posts/add",
        headers={"Content-Type": "application/json"},
        json={"userId": user_id, "id": id, "title": title},
    )
    
    return response.json()
