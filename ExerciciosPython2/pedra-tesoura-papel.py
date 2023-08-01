while True:
    jogador1 = input("Jogador 1, escolha entre Pedra, Papel ou Tesoura: ").lower()
    jogador2 = input("Jogador 2, escolha entre Pedra, Papel ou Tesoura: ").lower()

    if jogador1 == jogador2:
        print("Empate!")
    elif jogador1 == "pedra":
        if jogador2 == "tesoura":
            print("Jogador 1 venceu! Pedra quebra Tesoura.")
        else:
            print("Jogador 2 venceu! Papel cobre Pedra.")
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            print("Jogador 1 venceu! Papel cobre Pedra.")
        else:
            print("Jogador 2 venceu! Tesoura corta Papel.")
    elif jogador1 == "tesoura":
        if jogador2 == "pedra":
            print("Jogador 2 venceu! Pedra quebra Tesoura.")
        else:
            print("Jogador 1 venceu! Tesoura corta Papel.")
    else:
        print("Jogada inválida! Por favor, escolha entre Pedra, Papel ou Tesoura.")

    resposta = input("Desejam jogar novamente? (s/n): ").lower()
    if resposta != "s":
        break
