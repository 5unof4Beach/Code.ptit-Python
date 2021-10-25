from User import User

user1 = User("Duc", "Bui", 20)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)