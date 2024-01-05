# Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

password = 'pwd'
chance = 3

str1 = input('Enter you Password: ')

while chance:
    if str1 == password:
        print('Welcome')
        break
    
    else:
        print('Wrong Password')
        print(f"{chance} attempts left")
        
        if chance:
            str1 = input('Re Enter you Password: ')
            chance -= 1
            
            if str1 == password:
                print(':::: Welcome ::::')
                break
    
# resolved
