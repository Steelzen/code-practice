my_hash_map = {}

my_hash_map[4] = 83
print(my_hash_map[4]) # Prints 83

print(4 in my_hash_map) # Prints True
print(854 in my_hash_map) # Prints False

my_hash_map[8] = 327
my_hash_map[45] = 82523

for key, val in my_hash_map.items():
    print(f"{key}: {val}")