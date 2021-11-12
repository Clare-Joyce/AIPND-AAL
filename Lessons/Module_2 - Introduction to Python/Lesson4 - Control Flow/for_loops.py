# Quick Brown Fox
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for i in sentence:
    print(i)
    
# Multiples of 5  
# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for i in range(5, 31, 5):
    print(i)


# Create Usernames
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in names:
    usernames.append(i.lower().replace(' ', '_'))

print(usernames)

# Modify Usernames with Range
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(0, len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ', "_")
    
print(usernames)


# Tag Counter
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for text in tokens:
    if text.endswith(">") and text.startswith("<"):
        count += 1
print(count)


# Create an HTML list
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for i in items:
    html_str = html_str +"<li>"+i+"</li>\n"

html_str = html_str + "</ul>"
print(html_str)


# Iterating through a Dictionary
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))


# Fruit Basket - Task 1
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit in basket_items:
#if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits:
        result += basket_items[fruit]
print(result)

# Fruit Basket - Task 2
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for fruit in basket_items:
#if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits:
        result += basket_items[fruit]
print(result)


#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for fruit in basket_items:
#if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits:
        result += basket_items[fruit]
print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for fruit in basket_items:
#if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits:
        result += basket_items[fruit]
print(result)



# Fruit Basket - Task 3
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for item in basket_items:
#if the key is in the list of fruits, add to fruit_count.
    if item in fruits:
        fruit_count += basket_items[item]
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += basket_items[item]

print(fruit_count, not_fruit_count)


# Practice Loops
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for num in check_prime:
    num_factors = [i for i in range(2, num) if num%i == 0]
    if len(num_factors) != 0:
        print("{} is NOT a prime number, because {} is a factor of {}".format(num, num_factors[0], num))
    else:
        print("{} is a prime number".format(num))
        