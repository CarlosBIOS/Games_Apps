class User:

    def __init__(self, user_id, username):
        print('The new user being created...')
        self.username = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def __str__(self):
        return 'Create a new user to social media'

    def follow(self, user):
        user.followers += 1
        self.following += 1


carlos = User('11', 'CarlosJJV')
cristina = User('0', 'Cris')

print(carlos.followers)  # 0
print(cristina.followers)  # 0
print(carlos.following)  # 0
print(cristina.following)  # 0

carlos.follow(cristina)

print(carlos.followers)  # 0
print(cristina.followers)  # 1
print(carlos.following)  # 1
print(cristina.following)  # 0

