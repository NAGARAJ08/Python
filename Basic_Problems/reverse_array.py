def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1


s = input("Enter the String to be reversed: ")
print(s)

ans =reverse_for_loop(s)

print("After reversing")
print(ans)