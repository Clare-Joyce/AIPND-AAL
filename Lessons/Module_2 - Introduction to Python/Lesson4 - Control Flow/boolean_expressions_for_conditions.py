altitude = 10000
speed = 250
propulsion = "Propeller"

print(altitude < 1000 and speed > 100)
print((propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000)
print(not (speed > 400 and propulsion == "Propeller"))
print((altitude > 500 and speed > 100) or not propulsion == "Propeller")


# Using Truth Values of Objects
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