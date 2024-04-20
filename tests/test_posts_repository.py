# from lib.posts_repository import *
# from lib.posts import *

# """
# When I call the all method on the UserAccountsRepository
# I get all user accounts back in a list
# """

# def test_list_all_user_accounts_socials_two(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = PostsRepository(db_connection)
#     posts = repository.all()
#     assert posts == [
#         Posts(1, 'My Day', 'It was nice', 1000, 1), 
#         Posts(2,'My Day 2', 'It was great', 1000, 2), 
#         ]

# """
# # When we call AlbumRepository#find
# # We get a single Album object reflecting the seed data.
# # """
# def test_get_single_record_socials_two(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = PostsRepository(db_connection)

#     post = repository.find(2)
#     assert post == Posts(2,'My Day 2', 'It was great', 1000, 2)


# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """
# def test_create_record_socials(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = PostsRepository(db_connection)

#     repository.create(Posts(None, 'My Day 3', 'It was BRILLIANT', 1000, 2))

#     posts = repository.all()
#     assert posts == [
#         Posts(1, 'My Day', 'It was nice', 1000, 1), 
#         Posts(2,'My Day 2', 'It was great', 1000, 2), 
#         Posts(3,'My Day 3', 'It was BRILLIANT', 1000, 2)
#         ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record_socials(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = PostsRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     posts = repository.all()
#     assert posts == [
#         Posts(1, 'My Day', 'It was nice', 1000, 1), 
#         Posts(2,'My Day 2', 'It was great', 1000, 2), 
#         ]