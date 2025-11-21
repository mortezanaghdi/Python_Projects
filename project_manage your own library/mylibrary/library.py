class Library:
    def __init__(self, title, author=""):
        self.title = title
        self.author = author

    book_list = ["hello", "me", "my"]

    def add_book(self, title, author):
        self.title = title
        self.author = author
        self.book_list.append(self.title)
        print(f"book {self.title} written by, {self.author} is added to the library list")

    def remove_book(self, title):
        self.title = title
        if self.title in self.book_list:
            self.book_list.remove(self.title)
            print(f"book {self.title} is deleted from library list")
        else:
            print(f"{self.title} is not in the book list")


    def search_book(self, title):
        find = False
        self.title = title
        for i in range(len(self.book_list)):
            if self.title == self.book_list[i]:
                find = True
                print(f"we found {self.title} in our library list")
        if not find:
            print(f"we could not find {self.title} in our library list")


    def show_books(self):
        print("our library book list are:\n")
        for l in range(len(self.book_list)):
            print(f"{l+1} -> {self.book_list[l]}")


# b = Library("b")
#
# b.add_book("b2")
# b.remove_book("b2")
# b.search_book("b2")
# b.show_books()
