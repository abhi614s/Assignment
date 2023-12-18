# Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

password = 'h2o'
chance = 3
str1 = input('Enter you Password: ')

while chance:
    if str1 == password:
        print('Welcome')
        break
    else:
        str1 = input('Re Enter you Password: ')
        chance -= 1
