'''import hashlib
import itertools
import string

def md5_hash(text):
    
    return hashlib.md5(text.encode()).hexdigest()

def brute_force_md5(hash_to_crack, max_length=5):
    """Attempt to brute-force the given MD5 hash."""
    chars = string.ascii_lowercase + string.digits  
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            if md5_hash(guess) == hash_to_crack:
                return guess
    return None


hashed_password = "5d41402abc4b2a76b9719d911017c592" 
cracked_password = brute_force_md5(hashed_password)

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found")'''

import hashlib
import itertools
import string

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def brute_force_md5(hash_to_crack, max_length=5):
    chars = string.ascii_lowercase + string.digits 
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            if md5_hash(guess) == hash_to_crack:
                return guess
    return None

def main():

    hash_to_crack = input("Enter the MD5 hash to crack: ")
   
    max_length = int(input("Enter the maximum length of the password: "))

  
    cracked_password = brute_force_md5(hash_to_crack, max_length)

   
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found")

if __name__ == "__main__":
    main()