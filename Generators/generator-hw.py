import random
# Create a generator that generates the squares of some numbers up to some number n
def gensquares(n):
    for i in range(n):
        yield(i**2)

for num in gensquares(10):
    print(num)

# Create a generator that yields "n" random numbers between a low and high number (that are inputs)

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

# Use the iter() function to convert the string below into an iterator
s = 'hello'

s = iter(s)

print(next(s))

# If the output has the potential of using a large amount of energy.

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
