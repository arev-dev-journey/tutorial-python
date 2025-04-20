from collections import Counter, defaultdict, namedtuple

mylist = [1,2,1,1,1,2,2,2,3,3,3,3,3]

print(Counter(mylist))

mylist = ['a','a',10,10,10]

print(Counter(mylist))

print(Counter('aaaabbbbbbmmsmsjf'))

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.lower().split()))

letters = 'aaaabbbbbcccccccccccddddddddddddd'
c = Counter(letters)
print(c)

print(c.most_common(1))

print(list(c))

d = {'a':10}
print(d['a'])

d = defaultdict(lambda: 'defaultval')

print(d['q'])
print(d)

mytuple = (10,20,30)

print(mytuple[0])

Dog = namedtuple('Dog',['age','breed','name'])

sammy = Dog(age=5,breed='Husky',name='Sam')

print(type(sammy))

print(sammy)

print(sammy.age)

print(sammy.breed)
print(sammy.name)

print(sammy[0])
