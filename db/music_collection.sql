DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE albums (
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT REFERENCES artists(id),
    id SERIAL PRIMARY KEY
);