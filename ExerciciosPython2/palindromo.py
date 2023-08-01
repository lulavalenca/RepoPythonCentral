string = input("Digite uma palavra ou frase: ")

# Remove espaços em branco e converte para minúsculas
string = string.replace(" ", "").lower()

# Verifica se a string é um palíndromo
if string == string[::-1]:
    print("A string é um palíndromo!")
else:
    print("A string não é um palíndromo!")
