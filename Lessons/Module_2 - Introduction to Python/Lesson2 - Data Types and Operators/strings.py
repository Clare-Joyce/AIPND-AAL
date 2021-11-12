# TODO: Fix this string!
# ford_quote = 'Whether you think you can, or you think you can't--you're right.'
# Fixed
ford_quote = "Whether you think you can, or you think you can't--you're right."


#  Write a Server Log Message
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + " accessed the site " + url + " at " + timestamp + ".")


# len() function
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"
full_name  = " ".join([given_name, middle_names, family_name])
name_length = len(full_name) # todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)