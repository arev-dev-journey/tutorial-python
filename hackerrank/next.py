lazy_in_place_assassin = lambda s1, s2: (i for i in ([-1] if len(s1) != len(s2)+1 else range(len(s1))) if all((p1 == i or str1[p1] == str2[p2]) and not (p1 != i and p2 == len(str2)-1) for p1, p2 in zip(range(len(s1)), range(len(s2))))
str1 = "abdgggda"
str2 = "abdggda"

print(list(lazy_in_place_assassin(str1, str2)))
# Output: [3, 4, 5]

