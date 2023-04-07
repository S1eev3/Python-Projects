import sqlite3


# get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

# execute insert statement for supplied person data
with sqlite3.connect('sqlTest.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
          (45, 'Luigi', 'Vercotti'))
