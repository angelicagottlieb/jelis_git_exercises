from lib.blog_posts import *
from lib.blog_posts_repository import *
from lib.tags import *

def test_find_with_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostsRepository(db_connection)
    result = repository.find_by_tag('coding')
    assert result == [BlogPost(1, "How to use Git"), BlogPost(2, "Fun classes"), BlogPost(3, "Using a REPL"), BlogPost(7, "SQL basics")]
