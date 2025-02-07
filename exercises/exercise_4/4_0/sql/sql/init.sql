CREATE TABLE myh_applications (
    id SERIAL PRIMARY KEY,
    utbildningsnamn TEXT,
    skola TEXT,
    utbildningsomrade TEXT,
    kommun TEXT,
    ansokta INT,
    beviljade INT
);
