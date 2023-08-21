class User:
    def __init__(self, username, email, image_file):
        self.username = username
        self.email = email
        self.image_file = image_file

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Creating a User object
user = User(username='john_doe', email='john@example.com', image_file='profile.jpg')

# Printing the User object
print(user)
