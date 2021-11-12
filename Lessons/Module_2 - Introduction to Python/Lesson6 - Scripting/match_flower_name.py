# Write your code here
# create a dictionary from flowers.txt

def read_flowers(filename):
    flowers_dict = dict()
    with open(filename, 'r') as flowers:
        for line in flowers:
            letter = line.split(":")[0]
            flower = line.split(":")[1].strip()
            flowers_dict[letter] = flower
    return flowers_dict 

# HINT: create a function to ask for user's first and last name
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    try:
        selected_letter = first_name[0].upper()
        print(selected_letter)
        
    except Exception:
        selected_letter = last_name[0].upper()
        print(selected_letter)
        
    else:
        print("Invalid Name!")
        
    flowers_dict = read_flowers("flowers.txt")
    print(flowers_dict[selected_letter])
    print("Unique flower name with the first letter: {}".format(flowers_dict.get(selected_letter)))
    
if __name__=='__main__':
    main()
    

# print the desired output

