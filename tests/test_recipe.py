from lib.recipe import Recipe

"""
Recipe constructs with an id, name, cooking time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 20, 3)
    assert recipe.id == 1
    assert recipe.name == "Test Recipe"
    assert recipe.cooking_time == 20
    assert recipe.rating == 3

"""
We can format artists to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Recipe", 20, 3)
    assert str(recipe) == "Recipe(1, Test Recipe, 20, 3)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Test Recipe", 20, 3)
    recipe2 = Recipe(1, "Test Recipe", 20, 3)
    assert recipe1 == recipe2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
