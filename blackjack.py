import random 

# Calcula o valor total da mão
def valor_da_mao(mao):
    total = sum(mao)
    ases = mao.count(11)
    while total > 21 and ases:
        total -= 10  # Reduz valor do Ás de 11 para 1
        ases -= 1
    return total

# Sorteia uma carta do baralho

def comprar_carta():
    carta = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
    return carta

# Exibe a mão e o total de pontos do jogador ou da casa
def mostrar_mao(mao, dono="Jogador"):
    print(f"{dono}: {mao} -> Total: {valor_da_mao(mao)}")

# Função principal do jogo Blackjack
def blackjack():
    print("Bem-vindo ao Blackjack!")
    
    # Solicita o saldo inicial do jogador
    saldo = float(input("Informe seu saldo inicial: R$ "))
    saldo_inicial = saldo
    rodada = 1

    # Início do loop de rodadas
    while saldo > 0:
        print(f"\n--- Rodada {rodada} ---")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

        # Entrada da aposta do jogador
        try:
            aposta = float(input("Quanto deseja apostar? R$ "))
        except ValueError:
            print("Por favor, insira um valor numérico.")
            continue

        # Validação da aposta
        if aposta > saldo or aposta <= 0:
            print("Valor inválido. Aposte uma quantia positiva e dentro do seu saldo.")
            continue

        # Distribuição inicial de cartas para jogador e casa
        mao_jogador = [comprar_carta(), comprar_carta()]
        mao_casa = [comprar_carta(), comprar_carta()]

        mostrar_mao(mao_jogador)  # Mostra a mão do jogador

        # Turno do jogador: pode comprar mais cartas
        while True:
            if valor_da_mao(mao_jogador) > 21:
                print("Você estourou! Passou de 21.")
                break

            acao = input("Deseja comprar outra carta? (s/n): ").lower()
            if acao == 's':
                mao_jogador.append(comprar_carta())
                mostrar_mao(mao_jogador)
            elif acao == 'n':
                break
            else:
                print("Entrada inválida.")

        # Calcula os pontos atuais do jogador e da casa
        pontos_jogador = valor_da_mao(mao_jogador)
        pontos_casa = valor_da_mao(mao_casa)

        # Turno da casa: compra cartas até ter pelo menos 17 pontos
        if pontos_jogador <= 21:
            while pontos_casa < 17:
                mao_casa.append(comprar_carta())
                pontos_casa = valor_da_mao(mao_casa)

        # Exibe o resultado da rodada
        print("\n--- Resultado da rodada ---")
        mostrar_mao(mao_jogador)
        mostrar_mao(mao_casa, "Casa")

        # Verifica quem venceu
        if pontos_jogador > 21:
            saldo -= aposta
            print(f"Você perdeu R$ {aposta:.2f}")
        elif pontos_casa > 21 or pontos_jogador > pontos_casa:
            saldo += aposta
            print(f"Você ganhou R$ {aposta:.2f}")
        elif pontos_jogador == pontos_casa:
            print("Empate! Sua aposta foi devolvida.")
        else:
            saldo -= aposta
            print(f"Você perdeu R$ {aposta:.2f}")

        print(f"Saldo após a rodada: R$ {saldo:.2f}")

        # Verifica se o jogador ainda tem saldo
        if saldo <= 0:
            print("Seu saldo acabou. Fim de jogo.")
            break

        # Pergunta se deseja continuar jogando
        continuar = input("Deseja continuar jogando? (s/n): ").lower()
        if continuar != 's':
            break

        rodada += 1

    # Exibe saldo final e lucro/prejuízo
    lucro_total = saldo - saldo_inicial
    print(f"\nVocê saiu com R$ {saldo:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")

# Executa o jogo ao rodar o arquivo
blackjack()
