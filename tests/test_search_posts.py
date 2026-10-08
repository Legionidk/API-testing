from src.post_controller import search_posts


def test_search_love():
    result = search_posts(query="love", limit=10)

    for post in result["posts"]:
        assert (
            "love" in post["title"].lower()
            or "love" in post["body"].lower()
            or "love" in post["tags"].lower()
        )
