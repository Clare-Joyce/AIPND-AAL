
# Use the code editor below to answer the following questions about verse and 
# use Test Run to check your output in the quiz at the bottom of this page.

# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
# What is the length of the string variable verse?
print("Verse length: {}".format(len(verse)))
# What is the index of the first occurrence of the word 'and' in verse?
print("First occurrence of 'and': {}".format(verse.find("and")))
# What is the index of the last occurrence of the word 'you' in verse?
print("Last occurrence of 'you': {}".format(verse.rfind("you")))
# What is the count of occurrences of the word 'you' in the verse?
print("Count of 'you': {}".format(verse.count("you")))