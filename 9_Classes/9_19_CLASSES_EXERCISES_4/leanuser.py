class User:
    def __init__(self, first_name, last_name, email, gender, age):
        """Defining a new user class for regular website users"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.age = age
        self.login_attempt = 0

    def describe_user(self):
        """Printing summary of user information"""
        print("Printing the user information.")
        print(f"\t-First Name: {self.first_name.title()}")
        print(f"\t-Last Name: {self.last_name.title()}")
        print(f"\t-Email: {self.email}")
        print(f"\t-Age: {self.age}")
        print(f"\t-Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}. Welcome to our website!")

    def print_login_attempts(self):
        print(f"Login attempts: {self.login_attempt}")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0