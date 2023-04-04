
class User:
    # Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    # Define the object initialization
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account


    # Define methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
        

# Faculty and Student child class definitions
class Faculty(User):
    tenure = True
    department = 'Humanities'
    faculty_id = None

    # Define polymorphed login method of child class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_id = input("Enter your Faculty ID: ")
        if (entry_email == self.email and entry_id == self.faculty_id):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

    # Define the object initialization
    def __init__(self, name, email, password, account, tenure, department, faculty_id):
        self.name = name
        self.email = email
        self.password = password
        self.account = account
        self.tenure = tenure
        self.department = department
        self.faculty_id = faculty_id

class Student(User):
    student_year = 'Sophomore'
    student_gpa = 3.2
    student_id = None


    # Define polymorphed login method of child class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_id = input("Enter your Student ID: ")
        if (entry_email == self.email and entry_id == self.student_id):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

    # Define the object initialization
    def __init__(self, name, email, password, account, year, gpa, student_id):
        self.name = name
        self.email = email
        self.password = password
        self.account = account
        self.student_year = year
        self.student_gps = gpa
        self.student_id = student_id


if __name__ == "__main__":
    new_Student = Student("Jane Thomas", "jthomas@gmail.com", "password", "1234", "Senior", 3.6, "1234")
    new_Student.login()
