# Define a Dictionary

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5
population = {"Shanghai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5}


# get() with a default value
elements = {}
elements.get('dilithium') # returns None
elements['dilithium']  # returns KeyError: 'dilithium'
elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"

# Checking for Equality vs. Identity: == vs. is
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

animals = {'dogs': [20, 10, 15, 8, 32, 15], 
        'cats': [3,4,2,8,2,4], 
        'rabbits': [2, 3, 3], 
        'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['dogs'])
print(animals['dogs'][3])
print(animals[3])
print(animals['fish'])
print(animals[3])

# Adding values to a nested dictionary
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(elements)
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements)