# Mirach Erkol
# 11/23/2025
# CSD325-340A
# Assignment 8.2

'''Create a program that includes the following:
    1)Use the JSON load()  function to load the file into a Python class list.
    2)Create a function that loops through the .json class list and prints out each value, should look something like:
        Ripley, Ellen : ID = 45604 , Email = eripley@gmail.com
    #3)Output notification to the user that this is the original Student list.
    #4)Call your print function.
    #5)Add your last name, first name, fictional ID, and email to the class list using append().
    #6)Output notification to the user that this is the updated Student list.
    #7)Call your print function.
    #8_Use the JSON dump() function to append the new data to the .json file.
    #9_Output notification to the user that the .json file was updated.

Run the program and take a screenshot of the results. Paste that screenshot into your Word document.
Once the program runs, you should also see a notification that the student.json file has changed, with a choice to save or not. Take a screen shot of the notification and paste into your Word document.
Open the .json file and copy the contents, then paste that into your Word document.'''

import json

#1 Use the JSON load() function to load the file into a Python class list.
def load_students():
    with open("student.json", "r") as f:
        students = json.load(f)
    return students


#2 Create a function that loops through the .json class list and prints out each value.
def print_students(students):
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")


def main():

    #1 Use the JSON load() function to load the file into a Python class list.
    students = load_students()

    #3 Output notification to the user that this is the original Student list.
    print("Original Student list:")

    #4 Call your print function.
    print_students(students)
    print()

    #5 Add your last name, first name, fictional ID, and email to the class list using append().
    new_student = {
        "F_Name": "Mirach",
        "L_Name": "Erkol",
        "Student_ID": 12345,
        "Email": "mirach@bellevue.com"
    }
    students.append(new_student)

    #6 Output notification to the user that this is the updated Student list.
    print("Updated Student list:")

    #7 Call your print function.
    print_students(students)
    print()

    #8 Use the JSON dump() function to append the new data to the .json file.
    with open("student.json", "w") as f:
        json.dump(students, f, indent=4)

    #9 Output notification to the user that the .json file was updated.
    print("student.json file was updated.")


if __name__ == "__main__":
    main()