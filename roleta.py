import random  # Importa a biblioteca para gerar escolhas aleatórias (usada na roleta)

# Função principal do jogo
def jogo_de_aposta():
    print("Bem-vindo ao jogo de apostas!")

    # Solicita o saldo inicial do jogador
    saldo = float(input("Informe seu saldo inicial: R$ "))
    saldo_inicial = saldo  # Guarda o saldo original para calcular lucro no final
    rodada = 1  # Controla o número da rodada

    # Enquanto o jogador tiver saldo, continua jogando
    while saldo > 0:
        print(f"\n--- Rodada {rodada} ---")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

        # Solicita o valor da aposta e trata erros de entrada
        try:
            aposta = float(input("Quanto deseja apostar? R$ "))
        except ValueError:
            print("Por favor, insira um valor numérico.")
            continue

        # Verifica se a aposta é válida (positiva e menor ou igual ao saldo)
        if aposta > saldo or aposta <= 0:
            print("Valor inválido. Aposte uma quantia positiva e dentro do seu saldo.")
            continue

        # Pede para o jogador escolher uma cor
        escolha = input("Escolha uma cor para apostar (vermelho, preto ou branco): ").lower()

        # Valida se a cor escolhida é permitida
        if escolha not in ["vermelho", "preto", "branco"]:
            print("Escolha inválida. Tente novamente.")
            continue

        # Simula o resultado da roleta com probabilidades definidas
        roleta = random.choices(
            ["vermelho", "preto", "branco"],
            weights=[47, 47, 6],  # Probabilidades (branco é mais raro)
            k=1
        )[0]

        print(f"A roleta caiu em: {roleta.upper()}")  # Mostra o resultado da roleta

        # Verifica se o jogador ganhou
        if escolha == roleta:
            if roleta == "branco":
                ganho = aposta * 14  # Branco paga 14x
            else:
                ganho = aposta * 2   # Vermelho e preto pagam 2x
            saldo += ganho - aposta  # Adiciona o lucro ao saldo
            print(f"Parabéns! Você ganhou R$ {ganho - aposta:.2f}")
        else:
            saldo -= aposta  # Subtrai o valor apostado se perdeu
            print(f"Que pena! Você perdeu R$ {aposta:.2f}")

        print(f"Saldo após a rodada: R$ {saldo:.2f}")

        # Se o saldo acabou, encerra o jogo
        if saldo <= 0:
            print("Seu saldo acabou. Fim de jogo.")
            break

        # Pergunta se o jogador quer continuar jogando
        continuar = input("Deseja continuar apostando? (s/n): ").lower()
        if continuar != "s":
            break

        rodada += 1  # Incrementa a rodada

    # Mostra o saldo final e calcula o lucro
    lucro_total = saldo - saldo_inicial
    print(f"\nVocê saiu com R$ {saldo:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")

# Chamada da função para iniciar o jogo
jogo_de_aposta()
