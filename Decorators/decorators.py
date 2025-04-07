'''This is an intro to decorators in python'''
def func():
    return 1 

print(func)

def hello():
    return "Hello!"

print(hello())
print(hello)

greet = hello

print(greet())

del hello

print(greet())

def hello(name="Alex"):
    print('The hello() function has been executed')

    def greet():
        return '\t This is the greet() func inside hello'

    def welcome():
        return '\t This is the welcome() inside hello'
    print('I am going to return a function!')

    if name == "Alex":
        return greet
    else:
        return welcome

my_new_func = hello("Alex")
print(my_new_func())

def cool():

    def super_cool():
        return 'I am very cool!'
    return super_cool

some_func = cool()

print(some_func)

print(some_func())

def hello():
    return 'Hi Alex!'

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())

print(other(hello))

def new_decorator(original_func):

    def wrap_func():

        print("Some extra code, before the original function")

        original_func()

        print('Some extra code, after the original funciton')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

decorated_func = new_decorator(func_needs_decorator)

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()


