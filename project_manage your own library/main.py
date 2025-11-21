############### Building library a module #################

from mylibrary import library

if __name__ == "__main__":
    print("Welcome to our library Choose what you want to do:")
    print("1. Add book\n2. Remove book\n3. Show books\n4. Finish")
    action = input("Enter the number of what you like to do: ")
    action = int(action)
    my_instance = library.Library("my_instance")
    print()

    FINISH = False
    while not FINISH:
        if action == 1:
            print("You want to add a book to the library\nPlease Enter the title of the book or if you like add the author too")
            TITLE = ""
            while TITLE == "":
                print("you should add title")
                TITLE = input("Add title: ")
            author = input("Add author name (optional): ")
            my_instance.add_book(TITLE, author)
            anything_else = input("\nDo you like to do anything else? (Y/N) ")
            if anything_else.upper() == "Y":
                print("1. Add book\n2. Remove book\n3. Show books\n4. Finish")
                action = input("Enter the number of what you like to do: ")
                action = int(action)
            else:
                FINISH = True

        if action == 2:
            print("What do book do you want to delete from the list")
            TITLE = input("Add title: ")
            if TITLE != "":
                my_instance.remove_book(TITLE)
            anything_else = input("\nDo you like to do anything else? (Y/N) ")
            if anything_else.upper() == "Y":
                print("1. Add book\n2. Remove book\n3. Show books\n4. Finish")
                action = input("Enter the number of what you like to do: ")
                action = int(action)
            else:
                FINISH = True

        if action == 3:
            my_instance.show_books()
            anything_else = input("\nDo you like to do anything else? (Y/N) ")
            if anything_else.upper() == "Y":
                print("1. Add book\n2. Remove book\n3. Show books\n4. Finish")
                action = input("Enter the number of what you like to do: ")
                action = int(action)
            else:
                FINISH = True

        if action == 4:
            break

