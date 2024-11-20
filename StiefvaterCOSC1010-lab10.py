# Tyler Stiefvater
# UWYO COSC 1010
# Submission Date: 11/20/24
# Lab 10
# Lab Section: 15

from hashlib import sha256
from pathlib import Path

def get_hash(to_hash):
    """Generate SHA-256 hash of a given string."""
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()


hash_file_path = Path('hash')
rockyou_file_path = Path('rockyou.txt')

try:
    with hash_file_path.open('r') as hash_file:
        target_hash = hash_file.read().strip()
except FileNotFoundError:
    print("Error: 'hash' file not found.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred while reading 'hash': {e}")
    exit(1)

try:
    with rockyou_file_path.open('r', encoding='utf-8', errors='ignore') as rockyou_file:
        for line in rockyou_file:
            password = line.strip()  # Remove whitespace/newline
            hashed_password = get_hash(password)  # Hash the password
            
            # Compare the hashes
            if hashed_password == target_hash:
                print(f"Password found: {password}")
                break
        else:
            print("Password not found in the provided list.")
except FileNotFoundError:
    print("Error: 'rockyou.txt' file not found.")
except Exception as e:
    print(f"An unexpected error occurred while reading 'rockyou.txt': {e}")
