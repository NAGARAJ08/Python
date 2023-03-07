def anagram(str1,str2):

    s1 = [str1[i] for i in range(0,len(str1))]
    s1.sort()

    s2 = [str2[i] for i in range(0,len(str2))]
    s2.sort()

    if s1==s2:
        print("Yes! They are anagrams")
    else:
        print("Nope! not Anagrams")



s1 = input("Enter the First String: ")
s2 = input("Enter the second String: ")

anagram(s1,s2)
