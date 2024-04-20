from lib.blog_posts import *
from lib.tag_repo import *
from lib.tags import *

def test_find_with_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagsRepository(db_connection)
    result = repository.find_by_post(2)
    assert result == [Tags(1, 'coding'), Tags(4, 'education')]
