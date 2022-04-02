import getpass
import os
from query_master import query_master_pwd 
from menu import menu, create, find_accounts, find_email
from cryptography.fernet import Fernet

key = fernet.Fernet.generate_key()

print(key)

def main():
  print('''
Hello world! _|¨|_
  
Password manager - created by Henrique Nery
  ''')
  
  master_password = getpass.getpass("Master Password:\n").encode()
  
  query_master_pwd(master_password)
  
  choice = menu()
  while choice != 'q':
      if choice == '1':
          create()
          break
      if choice == '2':
          find_accounts()
          break
      if choice == '3':
          find_email()
          break
      else:
        os.system('clear')
        print(f'{choice} is a invalid option, try again...\n')
        choice = menu()
  
  print('''
  ---------
  Good bye!
  ''')
  
  exit()



main()