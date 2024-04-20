from lib.user_accounts import *

class UserAccountsRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from user_accounts')
        users = []
        for row in rows:
            item = UserAccounts(row["id"], row["username"], row["email"])
            users.append(item)
        return users
    
    def find(self, user_account_id):
        rows = self._connection.execute('SELECT * from user_accounts WHERE id = %s', [user_account_id])
        row = rows[0]
        return UserAccounts(row["id"], row["username"], row["email"])
    
        # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user_account):
        self._connection.execute('INSERT INTO user_accounts (username, email) VALUES (%s, %s)', [
                                 user_account.username, user_account.email])
        return None

    # Delete an artist by their id
    def delete(self, user_account_id):
        self._connection.execute(
            'DELETE FROM user_accounts WHERE id = %s', [user_account_id])
        return None
