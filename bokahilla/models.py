# -*- coding: utf-8 -*-

# Model - the business logic of the application

# The model is all to do with the data that's to be handled by the application
# and nothing to do with how it's presented / wired into the view
# functions that work with data (files, database, api etc.)

# very simple class
class Book:

    def __init__(self, number, name, info, author):
        self.number = number
        self.name = name
        self.info = info
        self.author = author
        #book.append(dict("number"))

# data
booklist = [
    Book(0, "Lord of the Rings", "info about lord of the rings", "kári"), Book(1, "Two towers", "info about two towers", "jón"),  Book(2, "Lukkuláki", "info about two lukkuláki", "Nonni")
]
book =[]
# Ath þarf að útfæra betur.
