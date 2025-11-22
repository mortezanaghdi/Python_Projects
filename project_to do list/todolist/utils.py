# modules will not start by their own they only start from main.py
if __name__ != "__main__":
    def want_to_continue(finish):
        """
        this function to let user add a character
        and let him/her continue and the programmer
        repeat itself
        """
        want_continue = input("Do you want to continue? (Y/N)\n")
        if want_continue.lower() == "n":
            finish = True
            print("See you soon!")
        return finish

else:
    print("This is a module, you can add it to your project.")



