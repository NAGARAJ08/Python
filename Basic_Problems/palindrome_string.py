def check_palindrome(string):
    
    S = string[::-1] #slicing
    
    if S==string:
        return "Yes its Plaindrome"
    else: 
        return "Nope it is not palindrome"



s = input("Enter the string to check for palindrome: ")

print(check_palindrome(s))