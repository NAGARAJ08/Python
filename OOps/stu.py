from Student import Student

stud1 = Student("ABC", "MS", 9, False)
stud2 = Student("BBC", "MBA", 7, True)

# print(stud1.name, stud1.is_on_Probation)
print("is", stud1.name, "on honor Roll: ", stud1.on_honor_roll())
print("is", stud2.name, "on honor Roll: ", stud2.on_honor_roll())