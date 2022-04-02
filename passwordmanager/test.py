from hash_master_pass import create_hash_master
import hashlib
import os
import getpass

def query_master_pwd(): 
    master_password_hash = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    master_password_input = getpass.getpass("Master Password:\n").encode()
    hash_input = hashlib.sha256(master_password_input).hexdigest()

    if hash_input == master_password_hash: 
      os.system('clear')
      print('You\'re in...\n')
    else:
      mensage = 'Get out of here!!!'
      print(mensage.upper())
      exit() 
query_master_pwd()