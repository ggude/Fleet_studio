# Fleet_studio

##Pre-requisites:

1) Python 3
2) Pip
3) virtualenv
4) postman
## Configuration:

1) Create and activate a virtual environment
2) Install the requirements
3) create required tables
4) start the server on local host
## APIs

Books
http://127.0.0.1:5000/books                 [POST Request ]  
HEADERS:  
Content-Type : application/json  
BODY :  
{  "book_id":
  "title":
  "author": 
  "genre":
  "decsription":
}
Libraries 
http://127.0.0.1:5000/libraries                          [POST Request ]  
HEADERS:  
Content-Type : application/json  
BODY:  
{  "library_id":
  "name":
  "city":
  "state":
  "postalcode":
}
Users
http://127.0.0.1:5000/users                          [POST Request ]  
HEADERS:  
Content-Type : application/json  
BODY:  
{  "user_id":
    "name":
}
Library_books
http://127.0.0.1:5000/library_books                          [PUT Request ]  
HEADERS:  
Content-Type : application/json  
BODY: 
{  "library_book_id":
   "library_id":
   "book_id":
   "last_library_activity_id":
}
Library_activities
http://127.0.0.1:5000/library_activities                         [PUT Request ]  
HEADERS:  
Content-Type : application/json  
BODY:
{  "library_activity_id":
   "user_id":
   "library_book_id":
   "checked_out_at":
   "checked_in_at":
}
   

