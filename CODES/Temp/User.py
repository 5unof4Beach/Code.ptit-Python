class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
        self.welcome_user()
        self.description_user()

    def description_user(self):
        print(f"{self.first_name} {self.last_name} {self.age}")

    def welcome_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
