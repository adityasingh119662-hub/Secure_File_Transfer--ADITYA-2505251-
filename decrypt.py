from cryptography.fernet import Fernet

# Load key
with open("key.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Read encrypted file
with open("received_encrypted_file", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt data
decrypted_data = fernet.decrypt(encrypted_data)

# Save decrypted file
with open("decrypted_sample.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully!")