def divide(a, b):
    result = a / b
    return result

"""
it is a simple test that i need it not to crash therefore I added every error to handle it
below I used a while loop to make sure every time user add sth wrong program show it the error
and then it let user to do it again until he/she sees the true result
"""
stop = False

while not stop:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        div_result = divide(num1, num2)
    except ZeroDivisionError as err:
        print(f"Error Occurred -> {err}")
    except ValueError as err:
        print(f"Error Occurred -> {err}")
    except Exception as err:
        print(f"Error Occurred -> {err}")
    else:
        print("program run successfully")
        print(f"Result: {div_result:.2f}")
        stop = True