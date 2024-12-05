class User:
    # initializes the attributes of the object, just variables associated with the final object, will run everytime
    # a new user is created
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # by setting it to a value,I don't need to pass when calling User
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.followers += 1


user_1 = User("001", "jonny")
user_2 = User("002", "emy")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
