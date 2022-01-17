from flask import Flask, request, jsonify
import json
import sqlite3

app=Flask(__name__)
def db_connection():
    conn= None
    try:
        conn= sqlite3.connect("database.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/books", methods=["GET", "POST"])
def books():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM book")
        books =[
            dict(book_id=row[0], title=row[1], author=row[2])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
    if request.method == "POST":
        new_title = request.form["title"]
        new_author= request.form["author"]
        sql= """ INSERT INTO book (title, author)
                VALUES (?, ?) """
        conn.execute(sql, (new_title, new_author))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully", 201
@app.route("/book/<int:book_id>", methods=["GET", "PUT", "DELETE"])
def single_book(book_id):
    conn=db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == "GET":
        
        cursor= conn.execute("SELECT * FROM book WHERE book_id=?", (book_id,))
        rows=cursor.fetchall()
        for r in rows:
            book=r
        if book is not None:
            return jsonify(book), 200
        else:
            return "something wrong", 404
    if request.method == "PUT":
        sql= """ UPDATE book
                 SET title=?,
                 author=?
                 WHERE book_id=?"""
        title = request.form["title"]
        author= request.form["author"]
        updated_book = {
            "book_id": book_id,
            "title": title,
            "author": author
        }  
        conn.execute(sql, (title, author, book_id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == "DELETE":
        sql= """ DELETE FROM book WHERE book_id=? """
        conn.execute(sql, (book_id,))
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200
@app.route("/libraries", methods= ["GET", "POST"])
def libraries():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM library")
        libraries = [
            dict(library_id=row[0], name=row[1], city=row[2], state=row[3])
            for row in cursor.fetchall()
        ]
        if libraries is not None:
            return jsonify(libraries)
    if request.method == "POST":
        new_name=request.form["name"]
        new_city=request.form["city"]
        new_state=request.form["state"]
        sql= """ INSERT INTO library (name, city, state)
                VALUES (?, ?, ?) """
        conn.execute(sql, (new_name, new_city, new_state))
        conn.commit()
        return f"library with the id: {cursor.lastrowid} created successfully", 201
@app.route("/library/<int:library_id>", methods=["GET", "PUT", "DELETE"])
def single_library(library_id):
    conn=db_connection()
    cursor = conn.cursor()
    library= None
    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM library WHERE library_id=?", (library_id,))
        rows=cursor.fetchall()
        for r in rows:
            library=r
        if library is not None:
            return jsonify(library), 200
        else:
            return "something wrong", 404
    if request.method == "PUT":
        sql= """ UPDATE library
                SET name=?,
                city=?,
                state=?
                WHERE library_id=?"""
        name= request.form["name"]
        city= request.form["city"]
        state=request.form["state"]
        updated_library = {
            "library_id": library_id,
            "name": name,
            "city": city,
            "state": state
        }
        conn.execute(sql, (name, city, state))
        conn.commit()
        return jsonify(updated_library)
    if request.method == "DELETE":
        sql= """ DELETE FROM library WHERE library_id=? """
        conn.execute(sql, (library_id,))
        conn.commit()
        return "The library with id: {} has been deleted.".format(id), 200
# USERS table ::
@app.route("/users", methods= ["GET", "POST"])
def users():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM user")
        users = [
            dict(user_id=row[0], name=row[1])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)
    if request.method == "POST":
        new_name=request.form["name"]
        sql= """ INSERT INTO user (name)
                VALUES (?) """
        conn.execute(sql, (new_name, ))
        conn.commit()
        return f"user with the id: {cursor.lastrowid} created successfully", 201
@app.route("/user/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def single_user(user_id):
    conn=db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM user WHERE user_id=?", (user_id,))
        rows=cursor.fetchall()
        for r in rows:
            user=r
        if user is not None:
            return jsonify(user), 200
        else:
            return "something wrong", 404
    if request.method == "PUT":
        sql= """ UPDATE user
                SET name=?
                WHERE user_id=?"""
        name= request.form["name"]
        updated_user = {
            "user_id": user_id,
            "name": name
        }
        conn.execute(sql, (name))
        conn.commit()
        return jsonify(updated_user)
    if request.method == "DELETE":
        sql= """ DELETE FROM user WHERE user_id=? """
        conn.execute(sql, (user_id,))
        conn.commit()
        return "The user with id: {} has been deleted.".format(id), 200 
# LIBRARY_BOOKS 
@app.route("/library_books", methods= ["GET"])
def library_books():
    conn=db_connection()
    cursor=conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM library_book")
        library_books = [
            dict(id=row[0], library_id=row[1], book_id=row[2])
            for row in cursor.fetchall()
        ]
        if library_books is not None:
            return jsonify(library_books)
@app.route("/library_activities/<int:user_id>"", methods= ["GET", "PUT"])
def single_library_activity(id):
    conn=db_connection()
    cursor = conn.cursor()
    library_activity= None
    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM library_activity WHERE user_id=?", (user_id,))
        rows=cursor.fetchall()
        for r in rows:
            library_activity=r
        if library_activity is not None:
            return jsonify(library_activity), 200
        else:
            return "something wrong", 404
    if request.method == "PUT":
        sql= """ UPDATE library_activity
                SET user_id=?,
                library_id=?,
                checked_out_at=?,
                checked_in_at=?
                WHERE library_activity_id=?"""
        conn.execute(sql)
        conn.commit()
        return jsonify(updated_library_activity)
    if request.method == "DELETE":
        sql= """ DELETE FROM library_activity WHERE library_activity_id=? """
        conn.execute(sql, (library_activity_id,))
        conn.commit()
        return "The library with id: {} has been deleted.".format(id), 200 

@app.route('/')
def home():
    return 'Hello World!' 

if __name__=='__main__':
    app.run(debug=True)

