import psycopg2
from config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users
(
	id serial PRIMARY KEY,
	user_name varchar(30) NOT NULL
);

CREATE TABLE movies
(
	id serial PRIMARY KEY,
	title varchar(256) NOT NULL,
	genres varchar(256) NOT NULL
);

CREATE TABLE links
(
	id serial PRIMARY KEY,
	fk_movie_id integer REFERENCES movies(id),
	imdb_id integer NOT NULL,
	tmdb_id integer NOT NULL	
);

CREATE TABLE ratings
(
	id serial PRIMARY KEY,
	fk_user_id integer REFERENCES users(id),
	fk_movie_id integer REFERENCES movies(id),
	rating integer NOT NULL,
	time_stamp integer NOT NULL
);

CREATE TABLE tags
(
	id serial PRIMARY KEY,
	fk_user_id integer REFERENCES users(id),
	fk_movie_id integer REFERENCES movies(id),
	tag varchar(256) NOT NULL,
	time_stamp integer NOT NULL
);"""
        )
        print("CREATE TABLE +")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")