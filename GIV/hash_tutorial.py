# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:23:22 2017

@author: kiawo


Hash Tutorial
"""

import hashlib

print(hashlib.algorithms_available)

#MD5, output in hex format
#hexdigest returns a HEX string representing the hash, in case you need the sequence of bytes you should use digest instead.
hash_object = hashlib.md5(b'Hello World')
print(hash_object)
print(hash_object.hexdigest())

#SHA1, output in hex format
hash_object = hashlib.sha1(b'Hello World')
print(hash_object)
print(hash_object.hexdigest())

"""
Practical example: hashing passwords

In the following example we are hashing a password in order to store it 
in a database. In this example we are using a salt. 
A salt is a random sequence added to the password string before using 
the hash function. The salt is used in order to prevent dictionary attacks and 
rainbow tables attacks. However, if you are making real world applications and 
working with users' passwords, make sure to be updated about the latest 
vulnerabilities in this field.

https://en.wikipedia.org/wiki/Salt_(cryptography)

"""

import uuid
import hashlib
 
def hash_password(password):
    # uuid is used to generate a random number
    #uuid4() creates a random UUID (universally unique identifiers)
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')