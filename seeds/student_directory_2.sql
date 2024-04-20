DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS cohorts CASCADE;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  student_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 1', '2023-05-01');
INSERT INTO cohorts (name, starting_date) VALUES ('Cohort 2', '2022-04-01');

-- had to do this after doing the above so I could fetch the correct IDs
INSERT INTO students (student_name, cohort_id) VALUES ('Jeli', 1);
INSERT INTO students (student_name, cohort_id) VALUES ('Elior', 2);
