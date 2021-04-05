from userdatabase import UserDatabase
from address import Address

run = True
myuserdatabase = UserDatabase()


def menu():
    global run
    print('-' * 40)
    print('Please select option \n (1)  Create user\n (2)  List users\n (3)  Exit')

    choice = input('Your choice: ').lower()

    if choice in ('1', '2', '3'):
        if int(choice) == 1:  # create user
            print('-' * 40)
            new_user_fname = input('Enter first name: ')
            new_user_lname = input('Enter last name: ')
            new_user_age = int(input('Enter age: '))
            new_user_street = input('Enter street: ')
            new_user_city = input('Enter city: ')

            #  create address object
            new_user_address = Address(new_user_street, new_user_city)

            #  create user object
            myuserdatabase.create_user(new_user_fname, new_user_lname, new_user_age, new_user_address)
            print('-' * 40)
        if int(choice) == 2:
            print(myuserdatabase)
        if int(choice) == 3:
            run = False
            print('Exiting...')
    else:
        print('Invalid choice')

while run:
    menu()