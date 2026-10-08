from src.post_controller import create_post


def test_create_post(shared_posts):
    for post in shared_posts:
        created_post = create_post(
            user_id=post["userId"],
            id=post["id"],
            title=post["title"],
        )

        assert (
            created_post["title"] == post["title"]
            and created_post["userId"] == post["userId"]
        )
