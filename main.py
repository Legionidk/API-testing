from src.post_controller import *

print("Creating new post:")
print(
    "\b",
    create_post(user_id=1, id=1, title="Test title"),
)

print("\nGetting posts by 'life' tag:")
for post in get_post_by_tag(tag="life")["posts"]:
    print("\b", post["tags"])

print("\nGetting posts with no limit:")
print("\b", len(get_posts()["posts"]))

print("\nGetting posts with limit=10:")
print("\b", len(get_posts(limit=10)["posts"]))

print("\nSearch posts with 'love' query:")
for post in search_posts(query="love", limit=10)["posts"]:
    print(
        "\b",
        "love" in post["body"].lower()
        or "love" in post["title"].lower()
        or "love" in post["tags"],
    )
