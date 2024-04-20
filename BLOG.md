# BLOG Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.


```
Nouns:
comments, content,  
posts, title, content 
authors, name 
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| posts                 | title, content
| comments                content, author_table p



## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: posts
id: SERIAL
title: text
content: text


Table: comments
id: SERIAL
content: text
comment_author: text 


 
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one POST have many COMMENTS? (Yes)
2. Can one COMMENT have many POSTS? (No)
2. Can one COMMENT_AUTHOR have many COMMENTS? (Yes)
Can one COMMENT have many COMMENT_AUTHORS? (No)

You'll then be able to say that:

1. **[Posts] has many [Comments]**
2. And on the other side, **[Comments] belongs to [Post]**
3. In that case, the foreign key is in the table [Comments]

1. **[Comment_Authors] has many [Comments]**
2. And on the other side, **[Comments] belongs to [Comment_Authors]**
3. In that case, the foreign key is in the table [Comments]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

```

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: student_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);


CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  content text,
  author_name text,
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```