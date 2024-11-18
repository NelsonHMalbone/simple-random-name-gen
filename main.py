import random

# opening the file so python can read file.

with open('names.txt') as file:
    # using readlines because it's a method that returns a list containing each line in the file as a list item
    content = file.readlines()

# using a random.choice we are able to choice a name randomly from the list we open above with content
name_ran = random.choice(content)

# with this we are using a f string to beable to print a message and using the variable we created above
# to print out the name
print(f'Randomly selected name: {name_ran}')