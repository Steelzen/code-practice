def my_function(x):
    return list(dict.fromkeys(x))

myList = ["a", "b", "c", "c", "c"]

print(my_function(myList))