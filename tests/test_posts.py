from lib.posts import *

"""
User Account constructs with an id, username and email
"""
def test_recipe_constructs_posts():
    post = Posts(1, 'Title', 'Content', 55, 2)
    assert post.id == 1
    assert post.title == 'Title'
    assert post.content == 'Content'
    assert post.number_of_views == 55
    assert post.user_account_id == 2

"""
We can format user accounts to strings nicely
"""
def test_recipes_format_nicely_again():
    post = Posts(1, 'Title', 'Content', 55, 2)
    assert str(post) == "Posts(1, Title, Content, 55, 2)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_recipes_are_equal_again():
    post1 = Posts(1, 'Title', 'Content', 55, 2)
    post2 = Posts(1, 'Title', 'Content', 55, 2)
    assert post1 == post2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
