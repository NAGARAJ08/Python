#  output = [output_exp for var in input_list if(var satisfies this condtion)]

'''
consider a situation where we need to make a list of even no from the given list 

'''

# this is how normally it is done
input_list = [1,2,3,4,10,13,11,12,18,20]

output_list = []

for i in input_list:
    
    if i%2==0:
        output_list.append(i)

print(output_list," by normal meth")

print()

# but with the comprehension it can fit into a single  line

output_comp  = [i for i in input_list if i%2==0]

print(output_comp," by comprehension meth")


# another example 

# lets create a new list from above list where the output list contains the square of nums

output_comp_sq = [i**2 for i in input_list]


print("\n",input_list)
print("Squared:\n")
print(output_comp_sq)