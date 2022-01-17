import sqlite3
conn=sqlite3.connect("database.sqlite")

cursor=conn.cursor()

#sql_q= """ CREATE TABLE book (
 #   book_id integer PRIMARY KEY,
  #  title text NOT NULL,
   # author text NOT NULL
#)"""
#cursor.execute(sql_q)
#sql_p = """ CREATE TABLE library (
 #       library_id integer PRIMARY KEY,
  #      name text NOT NULL,
   #     city text NOT NULL,
    #    state text NOT NULL
#)"""
#cursor.execute(sql_p)
#sql_r = """ CREATE TABLE user (
 #       user_id integer PRIMARY KEY,
  #      name text NOT NULL
#)"""

#cursor.execute(sql_r)
sql_t = """ CREATE TABLE library_book (
        library_book_id integer PRIMARY KEY,
        library_id integer,
        book_id integer,
        CONSTRAINT fk_library
        FOREIGN KEY (library_id) REFERENCES library(library_id)
        CONSTRAINT fk_book
        FOREIGN KEY (book_id) REFERENCES book(book_id)
)"""
cursor.execute(sql_t)
#sql= " DROP TABLE library_book"
#cursor.execute(sql)
sql_a = """ CREATE TABLE library_activity (
        library_activity_id integer PRIMARY KEY,
        user_id integer,
        library_book_id integer,
        checked_out_at TEXT DEFAULT CURRENT_TIMESTAMP,
        checked_in_at TEXT DEFAULT CURRENT_TIMESTAMP,
        CONSTRAINT fk_user
        FOREIGN KEY (user_id) REFERENCES user(user_id)
        CONSTRAINT fk_library_book
        FOREIGN KEY (library_book_id) REFERENCES library_book(library_book_id)
)"""
cursor.execute(sql_a)