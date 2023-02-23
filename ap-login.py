#https://www.youtube.com/watch?v=O69N6Gk3eaw

#imports
import time

username = 'alan'
password = 'secretpassword'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print('Access granted')
    print('Please wait...')
    time.sleep(5)
    print('OK...Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('You have security clearance. Pulling up all dem secrets!')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might want to check both fields')



#workaround to keep microsoft shell open by waiting for input. Stops the autoclose
input('Press ENTER to exit')