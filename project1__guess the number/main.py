import random

def welcome():
    print("Hello welcome to this guessing game")
    print("you should guess a number between 1 to 100")
    print("good luck")
    print()

def finish(computer_num , number_of_try, fastest_guess):
    print()
    print(f"great, the number was {computer_num} and you guessed it in {number_of_try} try. your fastest guess was {fastest_guess} time/times ")
    play_again = input("Do you want to play again? (Y/N)\n")
    if play_again in ["y", "Y"]:
        continue_playing = True
    else:
        continue_playing = False
    return continue_playing

def get_a_guess():
    num = int(input("Enter a number: "))
    return num

def answer(num1, num2):
    if num1 > num2:
        return "Add a higher number."
    elif num1 < num2:
        return "Add a lower number."
    else:
        return win(num1, num2)

def win(num1, num2):
    if num1 == num2:
        return "You win!"


welcome()
continue_playing = True
guess_memory = []

while continue_playing:

    computer_number = random.randint(1, 100)
    # print(computer_number)
    guess = 0
    count = 0
    fastest_guess = 0

    while not win(computer_number, guess):
        guess = get_a_guess()
        count += 1
        print(answer(computer_number, guess))
    guess_memory.append(count)
    fastest_guess = min(guess_memory)
    continue_playing = finish(guess, count, fastest_guess)
