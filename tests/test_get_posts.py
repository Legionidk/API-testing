from src.post_controller import get_posts


def test_no_limit():
    assert len(get_posts()) > 0


def test_limit():
    assert len(get_posts(limit=10)["posts"]) == 10
