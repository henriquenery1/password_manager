from password_generator import password_gen
from db_manager import insert_data_table, consult_app, consult_email

def menu():
  print(('-' * 13) + 'Menu' + ('-' * 13))
  print('''
1. Create new password
2. Find all credentials of an app
3. Find all data of an email
q. Exit
  ''')
  print('-' * 30)
  return input('Choose an option: ')

##########################################

def create():
   app_name = str(input('Name of site or app you want to generate a password\n'))
  
   user_email = str(input('Please provide a user email for this app or site\n'))
  
   username = str(input('Please provide a username for this app or site (if applicable)\n'))
     
   url = str(input('Please paste the url to the site that you are creating the password\n'))  
  
   lenth = str(input('password length:\n'))
   if lenth == '':
     password_create = password_gen(40)
   else:  
    password_create = password_gen(int(lenth))
  
   print('-'*30)
   print(f'The password is:\n{password_create}')
   print('-'*30)
   
   print('Your password was copied to your database')
   print('-' *30)
  
   insert_data_table(app_name,password_create, user_email, username, url)
  
##########################################

def find_accounts():
   app = input('Please proivide the app that you want to find accounts for\n')
   consult_app(app)

##########################################

def find_email():
   email = input('Please proivide the name of the site or app you want to find the password to\n')
   consult_email(email)
   