import os
import pyaes

#Open file

file_name = 'Teste.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# decrypt key

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remove
os.remove(file_name)

#Create New file decrypt

new_file = 'Teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close