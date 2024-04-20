# from lib.user_accounts_repository import *
# from lib.user_accounts import *

# """
# When I call the all method on the UserAccountsRepository
# I get all user accounts back in a list
# """

# def test_list_all_user_accounts_socials(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = UserAccountsRepository(db_connection)
#     users = repository.all()
#     assert users == [
#         UserAccounts(1, 'Jeli', 'jeli@gmail.com'), 
#         UserAccounts(2, 'Elior', 'elior@hotmail.co.uk'), 
#         ]

# """
# When we call AlbumRepository#find
# We get a single Album object reflecting the seed data.
# """
# def test_get_single_record_socials(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = UserAccountsRepository(db_connection)

#     user = repository.find(2)
#     assert user == UserAccounts(2, 'Elior', 'elior@hotmail.co.uk')


# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """
# def test_create_record_socials(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = UserAccountsRepository(db_connection)

#     repository.create(UserAccounts(None, "Test User 2", "Test Email 2"))

#     users = repository.all()
#     assert users == [
#         UserAccounts(1, 'Jeli', 'jeli@gmail.com'), 
#         UserAccounts(2, 'Elior', 'elior@hotmail.co.uk'),
#         UserAccounts(3, 'Test User 2', 'Test Email 2'), 
#         ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record_socials(db_connection):
#     db_connection.seed("seeds/social-network-two.sql")
#     repository = UserAccountsRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         UserAccounts(1, 'Jeli', 'jeli@gmail.com'), 
#         UserAccounts(2, 'Elior', 'elior@hotmail.co.uk'), 
#         ]