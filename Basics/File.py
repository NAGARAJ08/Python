var = open("Raj.txt", "r")

print(var.readable())
print(var.writable())

# print(var.read())

# print(var.readline())
#
# print(var.readlines()[2])

for line in var.readlines():
    print(line)
var.close()
