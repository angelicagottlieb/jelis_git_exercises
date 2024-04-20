# ORDERS AND ITEMS - Two Tables (Many-to-Many) Design Recipe Template

_Copy this recipe template to design and create two related database tables having a Many-to-Many relationship._

*Going to try first with many-to-many and do it with one-to-many if it goes wrong*

## 1. Extract nouns from the user stories or specification

```

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.

```

```
Nouns:

items, name, price,, quantity_available
orders, customer_name, date 
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| items                 | name, price, quantity_available
| orders                  | customer_name, date

1. Name of the first table (always plural): `items` 

    Column names: `name`, `price`, `quantity_available`

2. Name of the second table (always plural): `orders` 

    Column names: `customer_name`, `date`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: items
id: SERIAL
name: text
price: int
quantity_available: int

Table: orders
id: SERIAL
customer_name: text
date: date object
```

## 4. Design the Many-to-Many relationship


```

1. Can one order have many items? YES
2. Can one item have many orders? YES
```

_If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case._

## 5. Design the Join Table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `items_orders`.

```
# EXAMPLE

Join table for tables: items and orders
Join table name: items_orders
Columns: item_id, order_id
```

## 6. Write the SQL.

```sql
-- EXAMPLE
-- file: posts_tags.sql

-- Replace the table name, columm names and types.

-- Create the first table.

DROP TABLE IF EXISTS items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS items_orders CASCADE;

CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  price int,
  quantity_available int
);

-- Create the second table.
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  date_of_order date 
);

-- Create the join table.
CREATE TABLE items_orders (
  item_id int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

INSERT INTO items (name, price, quantity_available) VALUES ('Pink Top', 10, 100);
INSERT INTO items (name, price, quantity_available) VALUES ('Blue Top', 15, 200);

INSERT INTO orders (customer_name, date_of_order) VALUES ('Jeli', '2023-05-01');
INSERT INTO orders (customer_name, date_of_order) VALUES ('Elior', '2023-05-02');

INSERT INTO items_orders (item_id, order_id) VALUES (1, 2)
INSERT INTO items_orders (item_id, order_id) VALUES (2, 2)
INSERT INTO items_orders (item_id, order_id) VALUES (1, 1)



```

## 7. Create the tables.

```bash
psql -h 127.0.0.1 database_name < posts_tags.sql
```