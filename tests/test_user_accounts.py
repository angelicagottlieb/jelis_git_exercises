from lib.user_accounts import *

"""
User Account constructs with an id, username and email
"""
def test_recipe_constructs():
    user = UserAccounts(1, 'Test User', 'Test Email')
    assert user.id == 1
    assert user.username == 'Test User'
    assert user.email == 'Test Email'

"""
We can format user accounts to strings nicely
"""
def test_recipes_format_nicely():
    user = UserAccounts(1, "Test User", "Test Email")
    assert str(user) == "UserAccounts(1, Test User, Test Email)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_recipes_are_equal():
    user1 = UserAccounts(1, "Test Recipe", "Test Email")
    user2 = UserAccounts(1, "Test Recipe", "Test Email")
    assert user1 == user2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
