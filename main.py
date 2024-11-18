import random

# opening the file so python can read file.

with open('names.txt') as file:
    content = file.readlines()


name_ran = random.choice(content)

print(f'Randomly selected name: {name_ran}')