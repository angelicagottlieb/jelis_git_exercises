from lib.recipe_repository import *
from lib.recipe import *

"""
When I call the all method on the RecipeRepository
I get all recipes back in a list
"""

def test_list_all_albums(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1, 'Pasta', 20, 3), 
        Recipe(2, 'Pizza', 30, 4), 
        Recipe(3, 'Salad', 40, 3), 
        Recipe(4, 'Tofu', 25, 2), 
        Recipe(5, 'Tempeh', 10, 5)
        ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)

    album = repository.find(4)
    assert album == Recipe(4, 'Tofu', 25, 2)


