
    DROP TABLE IF EXISTS posts;
    DROP TABLE IF EXISTS user_accounts CASCADE;
    
    CREATE TABLE user_accounts (
    id SERIAL PRIMARY KEY,
    username text,
    email text
    );
        
    
    CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    number_of_views int,
    -- The foreign key name is always {other_table_singular}_id
    user_account_id int,
    constraint fk_user_account foreign key(user_account_id)
        references user_accounts(id)
        on delete cascade
    );


INSERT INTO user_accounts (username, email) VALUES ('Jeli', 'jeli@gmail.com');
INSERT INTO user_accounts (username, email) VALUES ('Elior', 'elior@hotmail.co.uk');

-- had to do this after doing the above so I could fetch the correct IDs
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('My Day', 'It was nice', 1000, 1);
INSERT INTO posts (title, content, number_of_views, user_account_id) VALUES ('My Day 2', 'It was great', 1000, 2);
