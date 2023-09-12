import random

# Lista de perguntas engraçadas e suas respostas
questions_answers = [
    ("Por que o esqueleto não brigou com ninguém?","Porque ele não tem estômago para isso!"),
    ("O que o pato disse para a pata?","Você tem pata-lógico!"),
    ("Por que o elefante não usa computador?","Porque tem medo do mouse!"),
    ("O que um espelho falou para o outro?","Seu visconde-me!"),
    ("Por que a matemática é o bicho-papão?","Porque ela tem problemas!"),
    ("Por que o esqueleto saiu da festa?","Porque estava se sentindo um pouco ‘deslocado’!"),
]

def main():
    print("Bem-vindo ao Jogo de Perguntas Engraçadas!")
    print("Responda às perguntas com suas respostas engraçadas.\n")

    while True:
        question, answer = random.choice(questions_answers)
        input(f"Pergunta: {question}\nPressione Enter para ver a resposta...")
        print(f"Resposta: {answer}\n")

        play_again = input("Deseja jogar novamente? (s/n): ")
        if play_again.lower() != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    main()

