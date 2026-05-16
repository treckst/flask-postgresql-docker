USE flaskdb;

CREATE TABLE users (
    id INT SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    loaded DEFAULT current_timestamp
);