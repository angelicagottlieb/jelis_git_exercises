from lib.blog_posts import *


def test_blog_posts_constructs():
    posts = BlogPost(1, "My Blog")
    assert posts.id == 1
    assert posts.title == "My Blog"


def test_construct_formats_nicely_blogs():
    posts = BlogPost(1, "My Blog")
    assert str(posts) == "BlogPost(1, My Blog)"

def test_cohorts_are_equal_blogs():
    posts1 = BlogPost(1, "My Blog")
    posts2 = BlogPost(1, "My Blog")
    assert posts1 == posts2