from lib.blog_posts import *
from lib.tags import *

class PostsRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        blog_posts = []
        for row in rows:
            item = BlogPost(row["id"], row["title"])
            blog_posts.append(item)
        return blog_posts
    
    def find(self, post_id):
        rows = self._connection.execute('SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return BlogPost(row["id"], row["title"])
    
    def find_by_tag(self, tag_name):
        rows = self._connection.execute("SELECT posts.id, posts.title FROM posts JOIN posts_tags ON posts.id = posts_tags.post_id JOIN tags ON posts_tags.tag_id = tags.id WHERE tags.name = %s", [tag_name])
        blog_posts = []
        for row in rows:
            item = BlogPost(row["id"], row["title"])
            blog_posts.append(item)
        return blog_posts