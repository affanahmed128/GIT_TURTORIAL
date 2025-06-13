# A dictionary in Python is a mutable, unordered collection of key-value pairs. It allows fast lookups, modifications, and deletions.
# Keys must be unique and immutable (strings, numbers, tuples).
# Values can be any data type.

d = {'a': 1}
print(type(d))           # <class 'dict'>
print(d)                 # {'a': 1}

d1 = {'name': 'affan'}
print(d1['name'])        # affan

d2 = {1234: 'affan'}
print(d2[1234])        # affan

# l={1,2,3,4}
# print(l[2])  # ❌ TypeError: 'set' object is not subscriptable

# Use a list instead of a set
l = [1, 2, 3, 4]
print(l[2])              # ✅ Output: 3 (zero-based index)

# d3 = {[1, 2, 3]: "issue"}  # ❌ TypeError: unhashable type: 'list'
d3 = {(1, 2, 3): "issue"}    # ✅ Correct, tuples are hashable

# Duplicate key - only last value is kept
d4 = {'name': "messi", 'name': "neymar"}  # {'name': 'neymar'}

d5 = {
    'game': "football",
    'cup': "worldcup",
    'club': ["BAR", "MDR", "ACM", "JUV"]
}
print(d5['club'])        # ['BAR', 'MDR', 'ACM', 'JUV']
print(d5['club'][1])     # MDR

# Nested Dictionary
d6 = {
    'game': "football",
    'cup': "worldcup",
    'club': ["BAR", "MDR", "ACM", "JUV"],
    'member': ('affan', 'esha', 'ronit', 'nousheen'),
    'player': {'messi', 'ronaldo', 'zidane', 'neymar'},
    'goals': {'affan': 500, 'esha': 400, 'ronit': 300, 'nousheen': 200}
}
print(d6)
# {
#     'game': 'football',
#     'cup': 'worldcup',
#     'club': ['BAR', 'MDR', 'ACM', 'JUV'],
#     'member': ('affan', 'esha', 'ronit', 'nousheen'),
#     'player': {'ronaldo', 'zidane', 'neymar', 'messi'},  # set order may vary
#     'goals': {'affan': 500, 'esha': 400, 'ronit': 300, 'nousheen': 200}
# }

print(d6['goals'])       
# {'affan': 500, 'esha': 400, 'ronit': 300, 'nousheen': 200}

# Modifying Dictionary
d6['year'] = 2025
d6['game'] = 'cricket'
print(d6)
# Now includes:
# 'year': 2025 and 'game': 'cricket' instead of 'football'

# Deleting Elements
del d6['year']
print(d6)
# 'year' key removed

# Dictionary Methods
print("Dictionary Methods")
print(list(d6.keys()))   
# ['game', 'cup', 'club', 'member', 'player', 'goals']

print(d6.keys())         
# dict_keys(['game', 'cup', 'club', 'member', 'player', 'goals'])

print(list(d6.values())) 
# ['cricket', 'worldcup', ['BAR', 'MDR', 'ACM', 'JUV'], ('affan', 'esha', 'ronit', 'nousheen'), {...}, {...}]

print(d6.items())        
# dict_items([('game', 'cricket'), ('cup', 'worldcup'), ...])

d7 = d6.copy()
print(d7)
# Copied dictionary contents

# Iterating in dictionary
print("ITERATION:")
for key, value in d6.items():
    print(f"{key}: {value}")
# Output:
# game: cricket
# cup: worldcup
# club: ['BAR', 'MDR', 'ACM', 'JUV']
# member: ('affan', 'esha', 'ronit', 'nousheen')
# player: {...}
# goals: {...}

# Clearing Dictionary
d6.clear()
print(d6)                # {}
print("hello fellas")