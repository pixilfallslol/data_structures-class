"""# Project: Library Management System

fruits = ['orange', 'banana', 'grapes', 'strawberry']
#counter = 1

# Can you use a a loop to show the number of fruits with a serial number?

for i in fruits:
    print(counter, i)
    counter += 1
    
for idx, fruit in enumerate(fruits, start = 1):
    print(idx, fruit)"""
    
"""class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isBorrowed = False # Checks if the book is borrowed.
        
    def borrowing(self):
        if not self.isBorrowed:
            self.isBorrowed = True # Its borrowed now YAY!
            return True
        return False
    
class Library:
    def __init__(self):
        self.books = [Book('Matilda', Author('Roald Dahl'))]
        # TODO: Add more books.
        
book1 = Book('Matilda', 'Roald, Dahl')

print(book1.borrowing())
print(book1.borrowing())"""

#Project: Library Management System

# fruits = ["orange","banana","grapes","strawberry"]

#can you use a loop to show the number of fruits with a serial number?

# 1. orange
# 2. banana

# counter = 1

# for i in fruits:
#     print(counter,i)
#     counter +=1

# #enumerate function 

# for i,fruit in enumerate(fruits,start =1):
#     print(i,fruit)

#Project: Library Management System

# fruits = ["orange","banana","grapes","strawberry"]

#can you use a loop to show the number of fruits with a serial number?

# 1. orange
# 2. banana

# counter = 1

# for i in fruits:
#     print(counter,i)
#     counter +=1

# #enumerate function 

# for i,fruit in enumerate(fruits,start =1):
#     print(i,fruit)

class Author:
    def __init__(self,name):
        self.name = name

class Book:
    def __init__(self,title,author):
        self.title = title 
        self.author = author 
        self.is_borrowed = False # is borrowed? False

    def borrowing(self):
        if not self.is_borrowed: # Checks if the book isnt borrowed
            self.is_borrowed = True # is borrowed? Yes
            return True # Success
        return False # Wasn't a success, the book is already borrowed
    def returning(self):
        if self.is_borrowed: # checks if the book is currently borrowed
            self.is_borrowed = False # is borrowed? not anymore!
            return True # Success
        return False # Wasn't a success, the book isn't borrowed so you can't return it
    

class Library:
    def __init__(self):
        self.books = [
            Book("Matilda",Author("Roald Dahl")),
            Book("Restart", Author("Gordon Korman")),
            Book("Tumtum & Nutmeg: Adventures Beyond Nutmouse Hall ",Author("Emily Bearn")),
            Book("Hatchet", Author("Gary Paulsen")),
            Book("Fish in a Tree", Author("Linda Mullaly Hunt"))
        ]
    def addbook(self, Book):
        self.books.append(Book)
    def display_books(self):
        for i, book in enumerate(self.books):
            if not book.is_borrowed:
                Status = "Available"
            else:
                Status = "Borrowed"
            print(f"{i+1}. {book.title} by {book.author.name} -- {Status}")

library = Library()
while True:
    input = input("Choose the following:\n 1. Display Books (1)\n")
    if input == "1":
        print("Here are the status of all books:")
        library.display_books()
        input = None
        break