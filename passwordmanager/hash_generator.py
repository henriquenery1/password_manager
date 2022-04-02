import hashlib

hash_master_password = hashlib.sha256(input('enter here the password you want the hash to be generated:\n').encode()).hexdigest()
print('-'*30)
print(f'''-*30      
This is the hash:
{hash_master_password}
      
copy and paste where it is needed
      ''')