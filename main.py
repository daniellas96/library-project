# library server project for automation task. 

# opject definition start here:

class Book :
    nextId = 1
    def __init__(self,title,author):

        self.id = Book.nextId
        Book.nextId += 1
        self.title = title 
        self.author = author 
        self.is_borrowed = False 

Books = []

class User:
    def __init__(self,id,name):

        self.id = id
        self.name = name 
        self.borrows = []

Users = []

class Author :
    def __init__(self,id,name):

        self.id = id
        self.name = name
        self.books = []

Authors = []

class Librarian :
    def __init__(self,id,name,password):

        self.id = id 
        self.name = name 
        self.password = password

Librarians = []

class Borrow :
    def __init__(self,userName,book,librarianName,borrow_date,return_date):

        self.userName = userName
        self.book = book
        self.librarianName = librarianName
        self.borrow_date = borrow_date
        self.return_date = None
        

Borrows = []

#library function start here.

#add book.
def addBook(title,author):
    b = Book(title,author)
    Books.append(b)

#add user.
def addUser(id,name):
    u = User(id,name)
    Users.append(u)

#add author.
def addAuthor(id,name):
    a = Author(id,name)
    Authors.append(a)

#add librarian.
def Librarian(id,name,password):
    l = Librarian(id,name,password)
    Librarians.append(l)

#borrow book.
def borrowBook(user,Book,librarian,borrow_date):
    br = Borrow(user,Book,librarian,borrow_date)
    Borrows.append(br)

#return book.
def returnBook(user,Book,return_date):
    for Borrow in Borrows:
        if Borrow.user == user and Borrow.Book == Book:
            Borrow.return_date = return_date


    

    











