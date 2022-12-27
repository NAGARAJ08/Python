Set = {1, 2, 'Hey', 4, 'Hello', 6, 'World', 6, 2}
print(Set)


# Accessing the element using looping
print("\n Elements of the set are:")
for i in Set:
    print(i, end="\n")
print()

print("Is 'HEY' available in set?","Hey" in Set)
print("Is '4' available in set?",4 in Set)
print("Is '24' available in set?",24 in Set)
