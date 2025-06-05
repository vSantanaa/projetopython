import random

# ---------- Funções de Utilidade ----------
def comprar_carta():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])  # 10 = J, Q, K; 11 = Ás

def valor_da_mao(mao):
    total = sum(mao)
    ases = mao.count(11)
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def mostrar_mao(mao, dono="Jogador"):
    print(f"{dono}: {mao} -> Total: {valor_da_mao(mao)}")

# ---------- Jogo de Roleta ----------
def jogar_roleta(saldo):
    print("\n--- Roleta ---")
    try:
        aposta = float(input("Quanto deseja apostar? R$ "))
    except ValueError:
        print("Por favor, insira um valor numérico.")
        return saldo

    if aposta > saldo or aposta <= 0:
        print("Aposta inválida.")
        return saldo

    escolha = input("Escolha uma cor para apostar (vermelho, preto ou branco): ").lower()
    if escolha not in ["vermelho", "preto", "branco"]:
        print("Escolha inválida.")
        return saldo

    roleta = random.choices(["vermelho", "preto", "branco"], weights=[47, 47, 6])[0]
    print(f"A roleta caiu em: {roleta.upper()}")

    if escolha == roleta:
        ganho = aposta * 14 if roleta == "branco" else aposta * 2
        saldo += ganho - aposta
        print(f"Parabéns! Você ganhou R$ {ganho - aposta:.2f}")
    else:
        saldo -= aposta
        print(f"Que pena! Você perdeu R$ {aposta:.2f}")

    return saldo

# ---------- Jogo de Blackjack ----------
def jogar_blackjack(saldo):
    print("\n--- Blackjack ---")
    try:
        aposta = float(input("Quanto deseja apostar? R$ "))
    except ValueError:
        print("Por favor, insira um valor numérico.")
        return saldo

    if aposta > saldo or aposta <= 0:
        print("Aposta inválida.")
        return saldo

    mao_jogador = [comprar_carta(), comprar_carta()]
    mao_casa = [comprar_carta(), comprar_carta()]

    mostrar_mao(mao_jogador)

    while True:
        if valor_da_mao(mao_jogador) > 21:
            print("Você estourou!")
            break

        acao = input("Deseja comprar outra carta? (s/n): ").lower()
        if acao == 's':
            mao_jogador.append(comprar_carta())
            mostrar_mao(mao_jogador)
        elif acao == 'n':
            break
        else:
            print("Entrada inválida.")

    pontos_jogador = valor_da_mao(mao_jogador)
    pontos_casa = valor_da_mao(mao_casa)

    if pontos_jogador <= 21:
        while pontos_casa < 17:
            mao_casa.append(comprar_carta())
            pontos_casa = valor_da_mao(mao_casa)

    print("\n--- Resultado ---")
    mostrar_mao(mao_jogador)
    mostrar_mao(mao_casa, "Casa")

    if pontos_jogador > 21:
        saldo -= aposta
        print(f"Você perdeu R$ {aposta:.2f}")
    elif pontos_casa > 21 or pontos_jogador > pontos_casa:
        saldo += aposta
        print(f"Você ganhou R$ {aposta:.2f}")
    elif pontos_jogador == pontos_casa:
        print("Empate. Aposta devolvida.")
    else:
        saldo -= aposta
        print(f"Você perdeu R$ {aposta:.2f}")

    return saldo

# ---------- Menu Principal ----------
def menu():
    print("Bem-vindo ao Cassino A&T!")
    saldo = float(input("Informe seu saldo inicial: R$ "))
    saldo_inicial = saldo
    rodada = 1

    while saldo > 0:
        print(f"\n=== Rodada {rodada} ===")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("Escolha o jogo:")
        print("1 - Roleta")
        print("2 - Blackjack")
        escolha = input("Digite o número do jogo desejado (ou 'sair' para encerrar): ").lower()

        if escolha == '1':
            saldo = jogar_roleta(saldo)
        elif escolha == '2':
            saldo = jogar_blackjack(saldo)
        elif escolha == 'sair':
            break
        else:
            print("Opção inválida.")
            continue

        if saldo <= 0:
            print("Seu saldo acabou. Fim de jogo.")
            break

        continuar = input("Deseja continuar jogando? (s/n): ").lower()
        if continuar != 's':
            break

        rodada += 1

    lucro_total = saldo - saldo_inicial
    print(f"\nVocê saiu com R$ {saldo:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")

# ---------- Início ----------
menu()
