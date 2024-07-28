# Encryption and Decryption

## What is Encryption?
Encryption is the process of converting human-readable plaintext to incomprehensible text, also known as ciphertext.

## How does encryption work?
Encryption is a mathematical process that alters data using an encryption algorithm and a key.
For example, if Alice sends the message "Hello" to Bob, but she replaces each letter in her message with the letter that comes two places later in the alphabet. Instead of "Hello," her message now reads "Jgnnq." Fortunately, Bob knows that the key is "2" and can decrypt her message back to "Hello."

## What is a key?
A key is a string of characters used within an encryption algorithm for altering data so that it appears random.

## Types of Encryption?
There are two main types: asymmetric encryption and symmetric encryption. <br /> 
In asymmetric encryption, there are two keys: one private key for decryption and one public key for encryption. 
In symmetric encryption, there is one key for both encryption and decryption

## What is an encryption algorithm?
An encryption algorithm is the method used to transform data into ciphertext. An algorithm will use the encryption key in order to alter the data in a predictable way, so that even though the encrypted data will appear random, it can be turned back into plaintext by using the decryption key. <br /> 

Common encryption algorithms:
* AES
* 3-DES (Triple DES)
* RSA

## How AES encryption works?
AES is a symmetric block ciper that includes three block ciphers or cryptographic keys:
* AES-128 uses a 128-bit key length to encrypt and decrypt message blocks.
* AES-192 uses a 192-bit key length to encrypt and decrypt message blocks.
* AES-256 uses a 256-bit key length to encrypt and decrypt message blocks.

## How Triple DES works?
Triple Data Encryption Standard (Triple DES) is a symmetric block cipher-based cryptography standard that uses fixed length keys with three passes of the DES algorithm

## How RSA works?
RSA is an asymmetric cryptographic algorithm. RSA utilizes a private and public key pair. The private key is kept secret and known only to the creator of the key pair, while the public key is available to anyone. Either the public or private key can be used for encryption, while the other key can be used for decryption. 

### Reference 
https://www.cloudflare.com/learning/ssl/what-is-encryption/
https://www.techtarget.com/searchsecurity/definition/Advanced-Encryption-Standard
https://www.splunk.com/en_us/blog/learn/rsa-algorithm-cryptography.html

