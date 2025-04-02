try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("A type error has occurred")
except:
    print("General Error")

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("All Done")

def ask():

    while True:
        try:
            result = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
        else:
            print(f"Thank you. Your number squared is: {result**2}" )
            break

ask()
