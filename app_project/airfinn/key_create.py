from cryptography.fernet import Fernet
import base64

# Generate a random 32-byte key
key = Fernet.generate_key()

# Encode the key in URL-safe Base64 format
encoded_key = base64.urlsafe_b64encode(key)

key = encoded_key.decode().split("=")[0]

# Print the encoded key
print("Fernet key:", key)