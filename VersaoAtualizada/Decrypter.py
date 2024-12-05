import os
import pyaes

# Solicitar o nome do arquivo a ser descriptografado
file_name = input("Informe o nome do arquivo a ser descriptografado: ")

try:
    # Abrir o arquivo criptografado em modo de leitura binária
    with open(file_name, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Solicitar e validar a chave de descriptografia
    key_input = input("Informe a chave de descriptografia (16, 24 ou 32 caracteres): ")
    if len(key_input) not in (16, 24, 32):
        raise ValueError("A chave deve ter 16, 24 ou 32 caracteres para ser válida no AES.")

    # Criar o objeto AES para descriptografar
    aes = pyaes.AESModeOfOperationCTR(key_input.encode('utf-8'))
    decrypted_data = aes.decrypt(encrypted_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o novo arquivo descriptografado
    new_file_name = "ArquivoDescriptografado.txt"
    with open(new_file_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Arquivo descriptografado com sucesso: {new_file_name}")

except FileNotFoundError:
    print("Erro: O arquivo especificado não foi encontrado.")
except ValueError as ve:
    print(f"Erro de validação: {ve}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
