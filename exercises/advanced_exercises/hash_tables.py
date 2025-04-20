my_hash_table = {}

# Add key value pairs
my_hash_table["apple"] = 5.99
my_hash_table["car"] = 20_999
my_hash_table["python"] = "a programming language"

# Access values
print(my_hash_table["car"])

print("car" in my_hash_table)

del(my_hash_table["car"])

print(my_hash_table.keys())
print(my_hash_table.values())

for key,value in my_hash_table.items():
    print(key, "->", value)

def word_counter(sentence):
    counter = {}
    words = sentence.split()

    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

print(word_counter("this is a test this is only a test"))

person = {
    "name": "Alex",
    "age": 25,
    "city": "Los Angeles"
}

print(person["name"])
person["email"] = "alex@example.com"

del person["city"]
print("name" in person)

for key, value in person.items():
    print(key, "->", value)

from collections import defaultdict, Counter

counter = defaultdict(int)

words = "hello world hello".split()

for word in words:
    counter[word] += 1

print(counter)

words = "apple orange banana apple orange apple".split()

counter = Counter(words)

print(counter)

person = {
    "name": "Bob"
}

print(person.get("age"))
print(person.get("age",0))

print(hash("apple"))

class Points:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x,self.y))

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

points = {}
p1 = Points(1,2)
p2 = Points(1,2)

points[p1] = "first point"

print(points[p2])

def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_repeated_char("abcad"))
print(first_repeated_char("abcdef"))

def twoSum(nums,target):
    seen = set()
    for num in nums:
        if(target - num) in seen:
            return (target - num , num)
        seen.add(num)
    return None

print(twoSum([2,7,11,15],9))

def group_anagrams(words):
    anagram_map = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbb"))
print(longest_unique_substring("pwwkew"))

count = {}
# def find_duplicates(nums):
#     duplicates = []
#
#     for num in nums:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
#
#     print("Frequency count:", count)
#     for num, freq in count.items():
#         if freq > 1:
#             duplicates.append(num)
#
#     return duplicates

def find_duplicates(nums):
    count = Counter(nums)
    duplicates = [num for num, freq in count.items() if freq > 1]
    return duplicates
print(find_duplicates([4,3,2,7,8,2,3,1]))

def top_k_frequent(nums, k):
    count = Counter(nums)

    return [item for item, freq in count.most_common(k)]
print(top_k_frequent([1,1,1,2,2,3],2))

def most_common_number(nums):
    return Counter(nums).most_common(1)[0][0]

print(most_common_number([1,2,3,2,4,2,5,3,3]))

def two_sum_hash(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i
    return []

print(two_sum_hash([10,5,2,7],12))
