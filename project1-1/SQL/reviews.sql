CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	review VARCHAR NOT NULL,
	rating INTEGER NOT NULL,
	book_id VARCHAR REFERENCES books (isbn) NOT NULL,
	user_id INTEGER REFERENCES users (id) NOT NULL
);


--- 1.Connect user and book with review id
--- 2.SELECT COUNT(book_id) FROM reviews WHERE book_id='0380795272';