# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library():
    def __init__(self,list_of_books):

        self.lend_data = {}
        #print(self.lend_data)
        self.list_of_books = list_of_books



        for books in self.list_of_books:
            self.lend_data[books] = None
        #print(self.lend_data)



    def display_books(self):
        print("These are the books in Library")
        for i in self.list_of_books:
            print(i)
        print("\n")

    def lend_books(self,author, book):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author

            else :
                print("This book is already lend to ", {self.lend_data[book]})

        else:
            print("Wrong entry")

    def return_book(self, book, author):

        if book in self.list_of_books:
            if self.lend_data is not None:
                print(book, "Book returned by" , author)
                self.lend_data[book] = None

            else:
                print("The name of the book you entered is wrong or not from this library")

        else :
            print("The name of the book you entered is wrong or not from this library")


    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name]=None
        print("Library after addition of the new book is \n", self.list_of_books)

    def delete_book(self,book_name):

        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)
        print("Book has been deleted")





def main():



    list_books=['Cookbook', 'Motu Patlu', 'Chacha_chaudhary', 'Rich Dad and Poor Dad']

    Deepak=Library(list_books)

    print("Type L for lend \n","Type A for ADD \n","Type R for Return \n","Type D for Delete \n","Type Dis for Display of all the books \n", "q for quit")


    Exit=False
    while(Exit is not True):
        print("Welcome : Kindly enter your choice\n")
        value=input()

        if value=="Dis":
            Deepak.display_books()

        elif value=="q":
            Exit=True
            print("Hope to see you again")

        elif value=="L":
            author = input("what is your name")
            books=input("Enter the name of the book you want")

            Deepak.lend_books(author,books)

        elif value=="A":
            newbook = input("Enter the name of the book you want to add")
            Deepak.add_book(newbook)

        elif value=="r":

            _a=input("Name of the book")
            _b=input("Your Name ")
            Deepak.return_book(_a, _b)

        elif value=="D":


            input1=input("Name of the book you want to delete")
            Deepak.delete_book(input1)


main()

