from user import User

class UserDatabase:
    user_list = []

    def __init__(self):
        print('Database created successfully')

    @staticmethod
    def create_user(fname, lname, age, address):
        UserDatabase.user_list.append(User(fname, lname, age, address))

    def __str__(self):
        print('-' * 40)
        print('User list:')
        users_string = ''
        for u in UserDatabase.user_list:
            users_string = users_string + u.firstname + ' ' + u.lastname + ' (' + str(u.age) + ')\n' + 'Address: ' + u.address.street + ', ' + u.address.city + '\n'
        return users_string

