CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    loaded TIMESTAMP DEFAULT current_timestamp
);