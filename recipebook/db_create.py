import sqlite3

conn = sqlite3.connect('db/recipebook.db')
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS person;
	DROP TABLE IF EXISTS recipes;
	DROP TABLE IF EXISTS recipes_notes;
	DROP TABLE IF EXISTS images;
	DROP TABLE IF EXISTS images_in_recipes;

	CREATE TABLE person (
	 	id integer PRIMARY KEY AUTOINCREMENT,
		login text,
		password text
	);

	CREATE TABLE recipes (
		id integer PRIMARY KEY AUTOINCREMENT,
		name text,
		description text,
		instruction text,
		ingredeints text
	);


	CREATE TABLE recipes_notes (
		person_id integer,
		recipe_id integer,
		note text,
		is_favourite integer
	);

	CREATE TABLE images (
		id integer PRIMARY KEY AUTOINCREMENT,
		image text
	);

	CREATE TABLE images_in_recipes (
		recipe_id integer,
		image_id integer
	);	
''')

conn.commit()
conn.close()


	