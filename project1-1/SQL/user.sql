CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	email VARCHAR NOT NULL,
	password VARCHAR NOT NULL
);

--- Check user already inserted or not
--- create domain alphanum as varchar(20) check (value ~ '^[A-Z0-9]+$'); 