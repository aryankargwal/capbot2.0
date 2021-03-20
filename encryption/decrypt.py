from cryptography.fernet import Fernet
fernet = Fernet(key) 
 
with open('result.csv', 'rb') as enc_file: 
    encrypted = enc_file.read() 

decrypted = fernet.decrypt(encrypted) 
  
with open('result.csv', 'wb') as dec_file: 
    dec_file.write(decrypted) 
