# Solicitação das duas listas ao usuário
lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()

# Remove possíveis elementos duplicados nas listas
lista1 = list(set(lista1))
lista2 = list(set(lista2))

# Criação da lista de elementos comuns
elementos_comuns = []

# Verifica se cada elemento da lista1 está presente na lista2
for elemento in lista1:
    if elemento in lista2:
        elementos_comuns.append(elemento)

# Exibe a lista de elementos comuns
print("Elementos comuns entre as duas listas:", elementos_comuns)
