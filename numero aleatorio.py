import random

def jogar():
    print("--- Bem-vindo ao número aleatório! ---")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        chute = int(input("Qual o seu chute? "))
        tentativas += 1

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            acertou = True
        elif chute < numero_secreto:
            print("Esse número é muito baixo. Tente um maior.")
        else:
            print("Esse número é muito alto. Tetnte um menor.")

if __name__ == "__main__":
    jogar()