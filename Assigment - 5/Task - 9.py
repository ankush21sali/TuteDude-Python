student = {
    "Alice" : 85,
    "Bob" : 65,
    "Jonh" : 70,
    "Jecob" : 53,
    "Harry" : 90,
    "Zatch" : 89
}

name = input("Enter The Student name : ")

if name in student:
    print(name + "'s Marks",student[name])
else:
    print("Student Not Found.")