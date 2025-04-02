def addNumbers(num1,num2):
    return num1 + num2

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))

print(addNumbers(number1,number2))

try:
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
except:
    print("Incorrect addition")
else:
    print("Add went well")
    print(result)

print("Something happened")


try:
    f = open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")

def ask_for_int():
    while True:
        try:
            result = int(input("Please enter a number: "))
        except:
            print("Invalid number")
            continue
        else:
            print("Yes, thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")

ask_for_int()
