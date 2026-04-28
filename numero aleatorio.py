import random

# Constantes facilitam a manutenção do código
LIMITE_INFERIOR = 1
LIMITE_SUPERIOR = 100

def jogar():
    print(f"--- Bem-vindo ao Jogo de Adivinhação! ---")
    print(f"Estou pensando em um número entre {LIMITE_INFERIOR} e {LIMITE_SUPERIOR}.")
    
    numero_secreto = random.randint(LIMITE_INFERIOR, LIMITE_SUPERIOR)
    tentativas = 0

    while True:
        try:
            chute = int(input(f"Qual o seu chute ({LIMITE_INFERIOR}-{LIMITE_SUPERIOR})? "))
            tentativas += 1

            if chute == numero_secreto:
                print(f"✅ Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif chute < numero_secreto:
                print("⬆️ Mais alto! Tente um número maior.")
            else:
                print("⬇️ Mais baixo! Tente um número menor.")
        
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    jogar()
