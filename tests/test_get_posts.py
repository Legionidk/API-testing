from src.post_controller import get_posts


def test_no_limit():
    assert len(get_posts()) > 0


def test_limit():
    assert len(get_posts(limit=10)["posts"]) == 10


def test_query():
    result = get_posts(query="love")
    for post in result["posts"]:
        assert (
            "love" in post["body"] or "love" in post["title"] or "love" in post["tags"]
        )
