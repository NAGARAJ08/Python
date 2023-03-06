# output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

# say we want a dict containig the odd nos along their cubes

input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

for i in input_list:
    
    if i%2!=0:
        output_dict[i] = i**3
        
print("using loop meth: ",output_dict)


# using the comprehension meth

output_dict_comp = {i:i**3 for i in input_list if i%2!=0}

print("using Comp, :",output_dict_comp)



# another example


state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']


out_dict = {}

for (key,value) in zip(state,capital):
    out_dict[key] = value
    
print("Using normal meth: ",out_dict)

out_dict_comp = {key:value for (key,value) in zip(state,capital)}

print("Using comp meth: ",out_dict_comp)