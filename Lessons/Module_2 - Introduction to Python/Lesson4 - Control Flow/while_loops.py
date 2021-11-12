# Factorials with While Loops
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


# Factorials with For Loops
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for i in range (1, number+1):
    product *= i

# print the factorial of number
print(product)

# Count By

start_num = 5#provide some start number
end_num = 50#provide some end number that you stop when you hit
count_by = 5#provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num

while break_num < end_num:
    break_num += count_by

print(break_num)



# Count By Check
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