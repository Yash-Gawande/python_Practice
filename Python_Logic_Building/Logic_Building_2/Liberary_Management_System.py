"""
*Problem Statement:

*Write a program that simulates a simple library management system. The system should allow users to:

Add books to the library
Remove books from the library
Search for books by title or author
Display all books in the library

*Requirements:

*The program should use a dictionary to store the books, where each book is represented by a dictionary with the following keys: title, author, and year.
*The program should have a menu-driven interface that allows users to interact with the library.
*The program should handle invalid inputs and provide error messages accordingly."""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        print("Book not found!")

    def search_book(self, search_term):
        results = [book for book in self.books if search_term in book.title or search_term in book.author]
        return results

    def display_books(self):
        for book in self.books:
            print(book)


books={}

while True:
    print("Library Management System")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search for book")
    print("4. Display all books")
    print("5. Exit")
    choice = input("Enter your choice: ")
    # Handle user input here
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter book year: "))
        books[title] = {"author": author, "year": year}
        print("Book added successfully!")
    elif choice == "2":
        title = input("Enter book title: ")
        if title in books:
            del books[title]
            print("Book removed successfully!")
        else:
            print("Book not found!")
    elif choice == "3":
        search_term = input("Enter book title or author: ")
        for title, book in books.items():
            if search_term in title or search_term in book["author"]:
                print(f"{title} by {book['author']} ({book['year']})")
    elif choice == "4":
        for title, book in books.items():
            print(f"{title} by {book['author']} ({book['year']})")
    elif choice == "5":
        break
    else:
        print("Invalid Input")
