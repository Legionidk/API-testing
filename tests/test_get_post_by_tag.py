import pytest
from src.post_controller import get_post_by_tag


def test_mystery_tag():
    result = get_post_by_tag(tag="mystery")
    for post in result["posts"]:
        assert "mystery" in post["tags"]


@pytest.mark.parametrize("tag", ["love", "crime", "history"])
def test_many_tags(tag):
    result = get_post_by_tag(tag=tag)
    for post in result["posts"]:
        assert tag in post["tags"]
