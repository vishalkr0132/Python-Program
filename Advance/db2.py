import re
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="student_info"
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS student_info")
cursor.execute("USE student_info")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
    name VARCHAR(255),
    age INT,
    phone VARCHAR(10),
    marks INT
)
''')

def validate_name(name):
    if re.match("^[A-Za-z][A-Za-z0-9]*$", name):
        return True
    else:
        print("Invalid name. It should not start with a number and can have alphanumeric characters.")
        return False

def validate_age(age):
    if age.isdigit() and int(age) > 0:
        return True
    else:
        print("Invalid age. It should be a positive integer.")
        return False

def validate_phone(phone):
    if re.match("^[0-9]{10}$", phone):
        return True
    else:
        print("Invalid phone number. It should contain exactly 10 digits.")
        return False

def validate_marks(marks):
    if marks.isdigit() and 35 <= int(marks) <= 100:
        return True
    else:
        print("Invalid marks. It should be in the range of 35 to 100.")
        return False

def insert_data(name, age, phone, marks):
    query = "INSERT INTO Student (name, age, phone, marks) VALUES (%s, %s, %s, %s)"
    values = (name, age, phone, marks)
    cursor.execute(query, values)
    conn.commit()
    print("Data inserted successfully!")

def accept_input():
    while True:
        name = input("Enter student name: ")
        if validate_name(name):
            break

    while True:
        age = input("Enter student age: ")
        if validate_age(age):
            break

    while True:
        phone = input("Enter student phone number: ")
        if validate_phone(phone):
            break

    while True:
        marks = input("Enter student marks: ")
        if validate_marks(marks):
            break

    insert_data(name, int(age), phone, int(marks))

def display_data():
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Name: {row[0]}, Age: {row[1]}, Phone: {row[2]}, Marks: {row[3]}")

def main():
    while True:
        print("\n1. Add Student Data")
        print("\n2. Display All Students")
        print("\n3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            accept_input()
        elif choice == '2':
            display_data()
        elif choice == '3':
            print("Exiting program...")
            conn.close()
            break
        else:
            print("Invalid choice, please try again.")

