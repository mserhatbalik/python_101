from leanuser import User

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"This user has the following privileges")
        while self.privileges:
            print(f"\t{self.privileges.pop()}")

class Admin(User):
    def __init__(self, first_name, last_name, email, gender, age):
        super().__init__(first_name, last_name, email, gender, age)
        self.privileges = Privileges()