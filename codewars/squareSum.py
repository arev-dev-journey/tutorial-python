# Square each number passed into it and then sum the result

def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

print(square_sum([1,2,3,4]))
