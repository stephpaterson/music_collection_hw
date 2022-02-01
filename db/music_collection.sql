DROP IF EXISTS album;
DROP IF EXISTS artists;

CREATE TABLE artists (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE album (
    title VARCHAR(255),
    genre VARCHAR(255),
    id SERIAL PRIMARY KEY
);