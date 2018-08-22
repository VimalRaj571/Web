CREATE TABLE books (
	isbn VARCHAR PRIMARY KEY,
	title VARCHAR NOT NULL,
	author VARCHAR NOT NULL,
	year INTEGER NOT NULL,
	review_count INTEGER ,
	average_score FLOAT 
);

--- 1.Connect with review
--- 2.Count the review using isbn FK
--- 3.ALTER TABLE (tablename) ALTER COLUMN (colname) TYPE VARCHAR