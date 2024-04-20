DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS items_orders CASCADE;


-- Create the second table.
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    date_of_order date 
    );
    
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name text,
    price int,
    quantity_available int
    );


-- Create the join table.
CREATE TABLE items_orders (
    item_id int,
    order_id int,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    PRIMARY KEY (item_id, order_id)
    );

INSERT INTO orders (customer_name, date_of_order) VALUES ('Jeli', '2023-05-01');
INSERT INTO orders (customer_name, date_of_order) VALUES ('Elior', '2023-05-02');

INSERT INTO items (name, price, quantity_available) VALUES ('Pink Top', 10, 100);
INSERT INTO items (name, price, quantity_available) VALUES ('Blue Top', 15, 200);

INSERT INTO items_orders (item_id, order_id) VALUES (1, 2), (2,2)
