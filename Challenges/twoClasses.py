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

class Student(User):
    student_year = 'Sophomore'
    student_gpa = 3.2




# Outside of the class you would create an instance of the User class
new_user = User()
# Call the login method using the new object
new_user.login()
