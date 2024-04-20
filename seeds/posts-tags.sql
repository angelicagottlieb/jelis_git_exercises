DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS tags CASCADE;
DROP TABLE IF EXISTS posts_tags CASCADE;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    );

-- Create the second table.
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name text
    );

-- Create the join table.
CREATE TABLE posts_tags (
    post_id int,
    tag_id int,
    constraint fk_movie foreign key(movie_id) references movies(id) on delete cascade,
    constraint fk_cinema foreign key(cinema_id) references cinemas(id) on delete cascade,
    PRIMARY KEY (movie_id, cinema_id)
    );