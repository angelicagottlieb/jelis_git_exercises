from lib.tags import *

class TagsRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def find_by_post(self, post_id):
        rows = self._connection.execute("SELECT tags.id, tags.name FROM tags JOIN posts_tags ON tags.id = posts_tags.tag_id JOIN posts ON posts_tags.post_id = posts.id WHERE posts.id = %s", [post_id])
        tags_list = []
        for row in rows:
            item = Tags(row["id"], row["name"])
            tags_list.append(item)
        return tags_list