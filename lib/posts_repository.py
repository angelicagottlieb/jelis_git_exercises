from lib.posts import *

class PostsRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Posts(row["id"], row["title"], row["content"], row["number_of_views"], row["user_account_id"])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute('SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Posts(row["id"], row["title"], row["content"], row["number_of_views"], row["user_account_id"])
    
        # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES (%s, %s, %s, %s)', [
                                 post.title, post.content, post.number_of_views, post.user_account_id])
        return None

    # Delete an artist by their id
    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None
