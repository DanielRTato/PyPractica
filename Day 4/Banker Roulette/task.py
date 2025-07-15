import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First option
random_number = random.randint(0,4)
print(friends[random_number])

# Second option
print(random.choice(friends))