from models.user import User

print("\nHello World")

# user = {
#     'name': 'John',
#     'birth': 1980,
# }
# user2 = {
#     'name': 'Helena',
#     'birth': 1995,
# }
# user3 = {
#     'name': 'Sandra',
#     'birth': 1978,
# }

# users = [user,user2,user3]

# for user in users:
#     print(user['name'],user['birth'])

# print(user['birth'],user2['birth'],user3['birth'])

user1 = User("Dani", 1990)
user2 = User("Maria", 1985)
user3 = User("Maria", 1985)

users = [user1,user2]

for user in users:
    print(user.name, user.birth, user.get_age(), user.is_adult())
