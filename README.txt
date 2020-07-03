************************************************STEPS*********************************************

1. Steps of Postgres: i)  sudo apt-get install postgresql postgresql-contrib
		     ii)  sudo su - postgres
		     iii) psql
		     iv)  CREATE ROLE root1 WITH LOGIN CREATEDB ENCRYPTED PASSWORD '123';
		      v)  CREATE DATABASE movies;
		     vi)  \c movies;
		     vii) CREATE TABLE "movies_movies" ("id" serial NOT NULL PRIMARY KEY, "title" varchar(100) , "poster_path" varchar(100) , "backdrop_path" varchar(100), "original_language" varchar(100), "original_title" varchar(1000), "overview" varchar(1000) , "release_date" varchar(100) , "popularity" integer, "vote_count" integer , "video" boolean , "adult" boolean , "genre_ids" integer[10]); 

		    viii) CREATE TABLE "movies_watchlist" ("id" serial NOT NULL PRIMARY KEY, "title" varchar(100) , "poster_path" varchar(100) , "backdrop_path" varchar(100), "original_language" varchar(100), "original_title" varchar(1000), "overview" varchar(1000) , "release_date" varchar(100) , "popularity" integer, "vote_count" integer , "video" boolean , "adult" boolean , "genre_ids" integer[10]);

#######################################################################################################

2. Steps for python: 
		python3 -m venv env

		. env/bin/activate

		pip install -r requirements.txt

		python manage.py migrate

		python manage.py runserver

		http://127.0.0.1:8000/graphql  run this on browser

#######################################################################################################

3. Steps for GhaphQL: Use "queries.graphql" file for run GraphQL APIs



