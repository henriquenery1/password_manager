from cryptography.fernet import Fernet

key = fernet.Fernet.generate_key()

print(key)
