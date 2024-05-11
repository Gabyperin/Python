

print("Seja bem vindo ao Hotel Eu e Você Quando Palace ⭐⭐⭐⭐⭐")

quantidade_pessoas = int(input("Quantas pessoas ficaram hospedadas? "))
hospedes = []

for pessoas in range(quantidade_pessoas):
    nome = str(input("Qual seu nome:"))
    cpf = int(input("Qual seu CPF? "))
    maior_de_idade = int(input("Para continuar o cadastro me informe sua idade: "))
    if maior_de_idade >= 18:
        print(f"OK,{nome}, idade suficiente para realizar a reserva, Obrigada :) ")
    else:
        print(f"Vaza daqui {nome}, vai procurar leite em outro lugar.")
    cadastro = [f"Nome:{nome}, CPF: {cpf}, {maior_de_idade} anos de idade"]
    hospedes.append(cadastro)

print(hospedes)
print(f"Divitam-se pombinhos")
