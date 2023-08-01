import random

# Gera um número aleatório entre 1 e 9
numero_secreto = random.randint(1, 9)

while True:
    # Solicita ao usuário para adivinhar o número
    adivinhacao = int(input("Adivinhe o número (entre 1 e 9): "))

    # Verifica se adivinhou corretamente
    if adivinhacao == numero_secreto:
        print("Parabéns! Você adivinhou corretamente.")
        break
    elif adivinhacao < numero_secreto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")
