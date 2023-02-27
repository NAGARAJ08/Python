cars = ["Benz", "BMW", "Porch", "TATA", "Maruti Suzuki"]
nums = [2, 45, 54, 56, 90, 23, 0, 123]

print(cars)
print(nums)

# functions

# copy
cars2 = cars.copy()
print(cars2)

# reverse
nums.reverse()
print(nums)

# sort
nums.sort()
cars.sort()
print(cars)
print(nums)

# insert
cars.insert(1, "Hyundai")
print(cars)

# remove
cars.remove("Hyundai")
print(cars)

# Append
nums.append(99)
print(nums)


cars.pop()
print(cars)

# print(cars.index("TATA"))

cars.append("TATA")

# Count
print(cars.count("TATA"))

# Extend
cars.extend(nums)
print(cars)




