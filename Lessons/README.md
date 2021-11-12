# Udacity_AIPPND
AI Programming with Python Nanodegree Program Sponsored by AAL (African App Launchpad)

### Module 2: Introduction to Python
#### Lesson 2: Data Types and Operators
* #### Arithmetic operators:
    - addition (+)
    - subtraction (-)
    - multiplication (*)
    - modular/remainder (%)
    - division (/)
    - integer division (//)
    - exponentiation (**)

*Note:* ^(the caret) does a bitwsie XOR operation not exponentiation

```python
# Quiz 1
# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement
print((23 + 32 + 64)/3)
```

```python
# Quiz 2
# Fill this in with an expression that calculates how many tiles are needed.
print((9*7)+(5*7))
# Fill this in with an expression that calculates how many tiles will be left over.
print((17*6)-((9*7)+(5*7)))
```
* #### Variables and Assignment Operators

```python
mv_population = 10000
# mv_populaiton = variable
# = is the assignment operator
# 10000 is the value assigned to mv_population
# mv_population is the name given to 10000
# Note: mv_population holds 10000 but 10000 does not hold mv_population

# 10000 can now be accessed from mv_population
```

```python
# Assigning multiple variables
# e.g
x, y, z = 2, 3, 5
```

```python
# more assignment operators
x += 2 (x = x + 2)
y -= 4 (y = y - 4)
z *= 5 (z = z * 5)
```
More Assignment operators can be found [here](https://www.programiz.com/python-programming/operators)

  **Naming variables in Python.**
  1. Names should be descriptive of their content
  2. Only use ordinary letters, numbers and underscores in your variable names.
  3. They can’t have spaces, and need to start with a letter or underscore.
  4. You can’t use Python's reserved words, or "keywords," as variable names.
  5. The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

```python
# Quiz 1

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= 0.1*rainfall
# add the rainfall variable to the reservoir_volume variable
reservoir_volume = rainfall + reservoir_volume
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume += 0.05*reservoir_volume
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= 0.05*reservoir_volume
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)
```

* #### Integers and floats
  - floats: fractions, decimal numbers
  - whole numbers
  - you can check the data type of a number or variable
```python
type(2.0) # float
type(variable_name)

x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
```
  
 * #### Booleans, Comparison Operators, and Logical Operators
  - True
  - False
  - <
  - (>)
  - (>=)
  - <=
  - ==
  - !=
  - AND
  - OR
  - NOT

```python
# Quiz
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
print(san_francisco_pop_density > rio_de_janeiro_pop_density)
```
* #### Strings
  - text
  - characters
  - quotes("")

```python
"Hello"
```

  - concatenate (+)
  - repeat string (*)
  - `len` returns the length of a string.
  - `len` returns a variable that can be stored in another variable

```python
# Quiz
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp + ".")
```

```python
# Quiz
middle_names = "Bradley"
family_name = "Pitt"
full_name  = " ".join([given_name, middle_names, family_name])
name_length = len(full_name) # todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
```

* #### Type and Type Conversion
  - int
  - float
  - string
  - bool
  - type casting

```python
# Quiz
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total = int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)
print("This week's total sales: " + str(total))
```

* #### String Methods
  - islower()
  - isupper()
  - count()
  - format()
  - find()
  - lower()
  - upper()

```python
# Quiz
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
```

* #### Debuggung
  - debugging is part of coding
  - understnad the errors
  - printing is highly recommended for debugging




#### Lesson 3: Data Structures

Containers of data
* #### Lists
  - mutable
  - ordered
  - sequence of elements in square brackets
  - mix of data types
  - look items up by using their index
  - zero-based indexing

```python
list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[0] # returns 1
list_of_random_things[-1] # returns True
list_of_random_things[-2] # reutrns a string
```

  - list slicing

```python
list_of_random_things[:2] # returns [1, 3.4]
```

  - Membership operators
    - in
    - not in

```python
'in' in 'this is a string' # returns True
'isa' in 'this is a string' # reutrns False
5 not in [1, 2, 3, 4, 6] # returns True
5 in [1, 2, 3, 4, 6] # returns False
```

  - lists can be modified but strings cannot be modified
  - both lists and strings are ordered, hence can be indexed

```python
# Quiz
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month-1]

print(num_days)
```
```python
# Quiz
clipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
# print(eclipse_dates)
print(eclipse_dates[-3:])
```

* #### List Methods
  - len()
  - max()
  - min()
  - sorted() returns a sorted copy of a list leaving the original list unchanged
  - join() joins items in a list
  - append() adds an item to a list

```python
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
# reutrns 
Albert & Ben & Carol & Donna
```

```python
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

# Output
["Albert", "Ben", "Carol", "Donna", Eugenia"]
```

*Note:* All data structures are data types

* #### Tuples
  - immutable ordered sequences of elements
  - tuple unpacking
  - you can't add and remove items from tuples, or sort them in place


* #### Sets
  - container of unique elements
  - mutable and unordered
  - supports membership operators
  - add() - adds an item to a set
  - pop() - removes the items(random item) from a set
  - union, intersection, difference are faster with sets than with other containers.


* #### Dictionaries
  - stores pairs of elements
  - maps unique keys to values
  - very handy when there is a key-value association
  - in and not in are used to check if a value exists in a dict or not
  - indices are not used to access elements in a dictionary, keys are used.
  - get() looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.
  - identity operators (is, is not)

*Note:* A dictionary key must be of a type that is immutable

```python
# Test the code here if you'd like
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

# returns
True
True
True
False
```

**Explanation**
List a and list b are equal and identical. List c is equal to a (and b for that matter) since they have the same contents. But a and c (and b for that matter, again) point to two different objects, i.e., they aren't identical objects. That is the difference between checking for equality vs. identity.

* #### Compound Data Structures
  - containers inside contaners

* #### Collections


* #### Quizzes

```python
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')
```

```python
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict.keys()
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(max(verse_dict.keys())) 
```


#### Lesson 4: Control Flow

* #### Conditional statements
  - if (contional expression required)
  - elif (contional expression required)
  - else

```python
points = 174  # use this input to make your submission

# write your if statement here
if 1 <= points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
    
elif 51 <= points <= 150:
    result = "Oh dear, no prize this time."
    
elif 151 <= points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
    
elif 181 <= points <= 200:
    result = "Congratulations! You won a penguin!"
    
print(result)

# Output
Congratulations! You won a wafer-thin mint!
```

```python
# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'NY'
purchase_amount = 10000

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

# Output
Since you're from NY, your total cost is 10890.0.
```

* #### Boolean expressions for conditions
  - if statement is a boolean expression that evaluates to either True or False.
  - Don't use True or False as conditions
  - Don't compare a boolean variable with == True or == False
  - The variable itself is a boolean expression
  - Truth value testing

*Some built-in objects that are considered False in Python:*

- constants defined to be false: None and False
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '"", (), [], {}, set(), range(0)

```python
points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"

elif 151 <= points <= 180:
    prize = "wafer-thin mint"
    
elif points >= 181:
    prize = "penguin"


if prize:
    result = "Congratulations! You won a "+prize+"!"
else:
    result = "Oh dear, no prize this time."

# use the truth value of prize to assign result to the correct prize
print(result)

# Output
Congratulations! You won a wafer-thin mint!
```

* #### For Loops
  - iterable objects return one element at a time

```python
usernames = []

# write your for loop here
for i in names:
    usernames.append(i.lower().replace(' ', '_'))

print(usernames)
```

```python
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in names:
    usernames.append(i.lower().replace(' ', '_'))

print(usernames)


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(0, len(usernames)):
    usernames[i] = usernames[i].lower().replace(' ', "_")
    
print(usernames)


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for text in tokens:
    if text.endswith(">") and text.startswith("<"):
        count += 1
print(count)


items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for i in items:
    html_str = html_str +"<li>"+i+"</li>\n"

html_str = html_str + "</ul>"
print(html_str)
```
* #### Building dictionaries

```python
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_count_dict = dict()
for word in book_title:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1
        
print(word_count_dict)
```

* #### Iterating Through Dictionaries with For Loops

*Note:* When you iterate through a dictionary using a for loop, doing it the normal way (for n in some_dict) will only give you access to the keys in the dictionary

```python
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
    
 
# Output
Iterating through keys:
Jason Alexander
Michael Richards
Jerry Seinfeld
Julia Louis-Dreyfus

Iterating through keys and values:
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes
```

* #### Quiz: Iterating Through Dictionaries


```python
# Quiz 1
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
```

```python
# Quiz 2

# If your solution is robust, you should be able to use it with any dictionary of 
# items to count the number of fruits in the basket

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
```

```python
# Quiz 3

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
# option 1
for item in basket_items:
#if the key is in the list of fruits, add to fruit_count.
    if item in fruits:
        fruit_count += basket_items[item]
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += basket_items[item]
       
 # option 2    
 for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print(fruit_count, not_fruit_count)
```


* #### While loops
  - for loops run for a redefined number of times(definite iteration).
  - while loops run for an unknown number of times (indefinite iteration).
  - they run as long as a certain condition is True.
  - and stop when the condition becomes False.
  - the while loop body should modify condition variable(s).

```python
# Use while loop
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:

    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

# Use for loop
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for i in range (1, number+1):
    product *= i

# print the factorial of number
print(product)
```

```python
# Count by
start_num = 10#provide some start number
end_num = 44 #provide some end number that you stop when you hit
count_by = 2#provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
if end_num > start_num:
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
    break_num = start_num
    
    while break_num < end_num:
        break_num += count_by
    
    result = break_num
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

print(result)


# Nearest Square
limit = 40

# write your while loop here
i = 1
while i**2 < limit:
    nearest_square = i**2
    i += 1

print(nearest_square)

```

```python
## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
# Option 1
i = 0
sum_list = 0
for num in num_list:
    if num%2 != 0 and i<5:
        # print(num)
        sum_list += num
        i += 1
        # print(i)

print(sum_list)

# Option 2, best optiona
count = 0
sum_list = 0
i = 0

while (count < 5) and (i < len(num_list)): 
    if num_list[i] % 2 != 0:
        sum_list += num_list[i]
        count += 1
    i += 1
    
print(sum_list)
```

*Note:* For loops iterate over every element in a sequence and while loops iterate until a stopping condition is met.
* #### Break and Continue 
  - When there is need for more precision on the stopping condition
  - A loop **terminates immediately** it comes across the break key word.
  - if you want to **skip a certain condition in a loop**, the continue keyword is used.

```python
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    # print(headline)
    news_ticker += headline + ' '
    print(len(news_ticker))
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(len(news_ticker))
print(news_ticker)
```

```python
# Identify prime numbers
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
```

* #### Zip and Enumerate
  - zip: returns an iterator that combines multiple iterables into one sequence of tuples.
  - enumerate: returns an iterator of tuples containing indices and values of a list.

```python
# Zip coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
coords = [i for i in zip(labels, x_coord, y_coord, z_coord)]
for i in coords:
    points.append("{}: {}, {}, {}".format(*i))
for point in points:
    print(point)
```

```python
# Zip lists to dictionary

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights)) # replace with your code
print(cast)
```

```python
# Unzip tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)
```

```python
# transpose with zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)
```

```python
# Enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, name in enumerate(cast):
    cast[i] = " ".join([name, str(heights[i])])

print(cast)
```

* #### List comprehensions
  - list creation with a for loop in one step
  - could involve conditions

```python
# Extract first names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [i.lower().split(' ')[0] for i in names] # write your list comprehension here
print(first_names)
```

```python
# Filter names by scores
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [i for i in scores if scores[i]>=65]# write your list comprehension here
print(passed)
```

```python
nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

### Question 1A: Create dictionary with the count of Oscar nominations for each director 
nom_count_dict = {}
# Add your solution code below before line 10. Add more lines for your code as needed.
for year, nominees in nominated.items():
    for nominee in nominees:
        if nominee not in nom_count_dict:
            nom_count_dict[nominee] = 1
        else:
            nom_count_dict[nominee] += 1
    


print("nom_count_dict = {}\n".format(nom_count_dict))
###################################################################################################################
###################################################################################################################

### Question 1B: Create dictionary with the count of Oscar wins for each director
win_count_dict = {}
# Add your solution code below before line 20. Add more lines for your code as needed.
for year, winns in winners.items():
    for winn in winns:
        if winn not in win_count_dict:
            win_count_dict[winn] = 1
        else:
            win_count_dict[winn] += 1


print("win_count_dict = {}".format(win_count_dict))


### For Question 2: Please provide a list with the name(s) of the director(s) with 
### the most Oscar wins. The list can hold the names of multiple directors,
### since there can be more than 1 director tied with the most Oscar wins.

# Add your code here
win_count_dict = {}
# Add your solution code below before line 20. Add more lines for your code as needed.
for year, winns in winners.items():
    for winn in winns:
        if winn not in win_count_dict:
            win_count_dict[winn] = 1
        else:
            win_count_dict[winn] += 1

most_win_director = [name for name in win_count_dict if win_count_dict.get(name) == max(win_count_dict.values())]

print("most_win_director = {}".format(most_win_director))

```

#### Lesson 5: Functions

* #### Defining functions
  - function header (def, name, parenthesis, arguments(optional, within()), :)
  - Function body (indented, variables declared within the body of the function are local variables)
  - return (optional, returns None by default, returns a value that can be assigned to a variable)
  - default argument values are used when the function call does not specify vales for the parameters.

```python

# write your function here
def population_density(population, land_area):
    return population/land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# write your function here
def readable_timedelta(days):
    weeks = days//7
    n_days = days%7
    return "{} week(s) and {} day(s).".format(weeks, n_days)
# test your function
print(readable_timedelta(1))
```

* #### Variable Scope
  - which parts of the program a varaible can be referenced from.
  - local and global scope
  - guides how info is passed through a program
  - variables with global scope can be accessed within functions
  - local variabes cannot be accessed outside a function
  - **it is best to define variables in the smallest scope they will be needed in**
  - **Python does not allow functions to modify variables outside the function's scope.**
  - Variables outside the function can only be read not changed or reassigned

* #### Documentation
   - Documentation strings, a type of comment
   - surrounded by triple quotes
   - brief description of the function's purpose
   - what the function needs and its output.

```python
def readable_timedelta(days):
    # insert your docstring here
    """Calculate number of weeks and days when given number of days.
    
    Args:
    days (int): number of days to be converted to weeks
    
    Returns:
    a string 
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)
```

* #### Lambda Expressions
  - They are used to create anonymous functions(functions without names)
  - very useful for functions that take other functions as arguments
  - Lambda keyword is used to indicate lambda expression, followed by the arguments, the column, then the expression.
  - very useful for short, simple functions
  - `map()`:  a built-in function that takes a function and an iterable and returns an iterator that applies the function to each item of the iterable.
  - `filter()`: a built-in function that takes a function and an iterable and returns an iterator with items for which the function is true.

```python
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
mean = lambda num_list: sum(num_list)/len(num_list)
averages = list(map(mean, numbers))
print(averages)


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

is_short = lambda name: len(name)<10
short_cities = list(filter(is_short, cities))
print(short_cities)
```

* #### Iterators and Generators
  - iterables: objects that one of their elements at a time(e.g list)
  - iterator: object that represents a stream of data
  - generators: a simple/powerful tool for creating iterators using functions
  - generators use the `yield` statement whenevr they want tp reutrn data
  - each time `next()` is called on it, it resumes where it left off
  - A generator can be created in the same way as a list except that () are used instead of []

```python
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    
    i = start
    for item in iterable:
        yield i, item
        i += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

def chunker(iterable, size):
    # Implement function here
    for i in range (0, len(iterable), size):
        yield iterable[i: i+size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
```

#### Lesson 6: Scripting

* #### Errors and Exceptions
    - Syntax Errors: occur when you don't use correct syntax and Python doesn't know how to run your code
    - Exceptions: occur when Python runs into unexpected situations while executing your code and can happen even if you used correct syntax.

* #### Handling Errors
    - try: the only mandatory clause in a try statement
    - except: runs if code in the try block fails
    - else: runs if the code in the try block does not fail
    - finally: runs this block under any conditions before leaving the try statement.

* #### Importing local Scripts
    - modules: python files with definitions and statements
    - To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if `__name__ == "__main__"` block
    - Avoid using `from module import *`
    - A package is a module that conatins sub modules and imported as `import package_name.submodule_name`
    - third party libraries can be installed with `pip`
    - *Note:* `pip install -r requirements.txt`
    - Good programmers master the task of finding information quickly


#### Lesson 6: Intro to OOP
* #### Procedural Programming(PP) vs OOP
    - PP: list of instructions beig executed
    - OOP: Programs built around objects
    - objects have characteristics and actions.

    ![pp_vs_oop](OOP/PP_vs_OOP.png)

