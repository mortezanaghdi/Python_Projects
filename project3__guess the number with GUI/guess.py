if __name__ != "__main__":

    import random

    class GuessGame:
        def __init__(self):
            self.computer_number = random.randint(1, 100)
            self.attempts = 0

        def check_guess(self, guess:int):
            self.attempts += 1

            if guess < self.computer_number:
                return "add higher number"
            elif guess > self.computer_number:
                return "add lower number"
            else:
                text = f"You win! The number was {self.computer_number} in {self.attempts} tries."
                # restart automatically
                self.__init__()
                return text

else:
    print("you should import it in your file")