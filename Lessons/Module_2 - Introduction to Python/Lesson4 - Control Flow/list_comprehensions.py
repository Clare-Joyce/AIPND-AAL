# Extract First Names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [i.lower().split(' ')[0] for i in names] # write your list comprehension here
print(first_names)


# Multiples of Three
multiples_3 = [i*3 for i in range(1, 21)]# write your list comprehension here
print(multiples_3)


# Filter Names by Scores
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [i for i in scores if scores[i]>=65]# write your list comprehension here
print(passed)