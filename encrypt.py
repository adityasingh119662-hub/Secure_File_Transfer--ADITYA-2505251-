from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Read original file
with open("sample.txt", "rb") as file:
    original_data = file.read()

# Encrypt data
encrypted_data = fernet.encrypt(original_data)

# Save encrypted file
with open("encrypted_sample.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")