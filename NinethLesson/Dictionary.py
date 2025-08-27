# this is basically objects from javascript

family_jargon = {
    "Family": "Consist of Femin, Fenas, Raji and Delna and Terra",
    "Partner": "Someone you want to marry",
    "Partner_name": "Find out already"
}

# to print any value from the dictionary, you can access them with key and its value will be printed
print(family_jargon["Partner"])

# the value can be replaced as well in dictionary
family_jargon["Partner_name"] = "Vimal Sagar Murali"
print(family_jargon)

# if a key we pass does not exist while trying to modify, it will create a new entry
family_jargon["I_want"] = "to be Married and be happy with 3 kids"
print(family_jargon)

# example program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 70:
        student_grades[student] = "Fail"
        
print(student_grades)