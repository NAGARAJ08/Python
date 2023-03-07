

def replace_five(s):
    S = ''
    for i in s:
        if i=='0':
            S = S+'5'
        else:
            S = S+i
    return S
            
    

s = input("Enter the data to replace the Zero's with '5''s ")

print(replace_five(s))
        
