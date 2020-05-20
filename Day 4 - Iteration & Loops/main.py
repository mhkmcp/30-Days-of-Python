my_list = [2, 5, 3, 5, 6, 7, 1]
print(my_list)

for val in my_list:
    print(val)

print()
for x in "123":
    print(x)

for x in range(1, 11):
    print(x)


user_1 = {'username': 'mhkm', 'id': 1}
user_2 = {'username': 'abcd', 'id': 2}

my_users = [user_1, user_2]

for user in my_users:
    print(user)

for user in my_users:
    print(user['username'])

user_2 = {'username': 'abcd', 'id': 2, 'email': 'abc@abc.abc'}

my_users = [user_1, user_2]
for user in my_users:
    # if 'email' in user.keys():
    if 'email' in user:
        print(user['email'])
    else:
        print("No Email")