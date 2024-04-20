DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS tags;

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name text,
);

-- Create the second table.
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_name text
);

-- Create the join table.
CREATE TABLE students_tags (
    student_id int,
    tag_id int,
    constraint fk_post foreign key(student_id) references students(id) on delete cascade,
    constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
    PRIMARY KEY (student_id, tag_id)
);
