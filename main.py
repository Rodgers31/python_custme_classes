class User:
    # initializes the attributes of the object, just variables associated with the final object, will run everytime
    # a new user is created
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "jonny")

print(user_1.username)

