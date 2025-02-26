# Missão 1

nota = float(input("Digite a nota do Aluno: "))

if nota >= 6:
    print("Aluno aprovado!!!")
elif nota <= 5:
    print("Aluno reprovado!!!")    


# Missão 2

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar!!!")
else:
    print("Você ainda não pode votar!")

# Missão 3

notaAluno = float(input("Digite sua nota: "))

if 90 <= notaAluno <= 100:
    print("Parabéns, você tirou A!")
elif 80 <= notaAluno < 90:
    print("Muito bem, você tirou B!")
elif 70 <= notaAluno < 80:
    print("Bom trabalho, você tirou C!")
elif 60 <= notaAluno < 70:
    print("Bom trabalho, você tirou D!")
else:
    print("Estude um pouco mais, você tirou F.")

# Missão 4

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2

print(f"A soma de {numero1} e {numero2} é {soma}.")

# Missão 5

senhaCorreta = "Python123"

senhaDigitada = input("Digite a senha: ")

if senhaDigitada == senhaCorreta:
    print("Acesso permitido!")
else:
    print("Acesso negado!")

    
# Missão 6

contagem = 1

while contagem <= 10:
    print(contagem)
    contagem += 1

# Missão 7

lista = [8, 3, 10, 1, 5]

lista.sort()

print(f"Números em ordem crescente:{lista}")

# Missão 8

alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")

print(f"Primeiro nome: {alunos[0]}")
print(f"Segundo nome: {alunos[-1]}")

# Missão 9

def dobro():
    numeroDobrar = float(input("Digite um número: "))
    print(f"O dobro de {numeroDobrar} é {numeroDobrar * 2}.")

dobro()

# Missão 10

def contarLetras(nome):
    quantidade = len(nome)
    print(f"O nome {nome} tem {quantidade} letras.")

nomeUsuario = input("Digite o nome: ")

contarLetras(nomeUsuario)



