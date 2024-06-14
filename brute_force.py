import itertools
import string
import time

def brute_force_password_cracker(password, max_length=100000000000):
    characters = string.ascii_letters  # conjunto de caracteres (letras maiúsculas e minúsculas)
    start_time = time.time()
    
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt = ''.join(attempt)
            if attempt == password:
                end_time = time.time()
                print(f"Senha encontrada: {attempt}")
                print(f"Tempo gasto: {end_time - start_time:.2f} segundos")
                return attempt
    print("Senha não encontrada dentro do limite de tentativas.")
    return None

# Defina a senha que deseja quebrar
password_to_crack = "ab"

# Chame a função de quebra de senha
brute_force_password_cracker(password_to_crack)
