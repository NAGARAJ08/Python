MonthConv = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "oct": "October",
    "Nov": "November",
    "Dec": "December",
}




print(MonthConv["Nov"])
print(MonthConv["Apr"])

print(MonthConv.get("Run","not a valid key"))