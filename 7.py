print ("_" * 80)

nome = input ("Digite o nome do aluno: ")

turma = input ("Digite a turma em que ele está: ")

n1 = float(input("Digite a primeira nota. "))

n2 = float(input("Digite a segunda nota. "))

n3 = float(input("Digite a terceira nota. "))

media = (n1 + n2 + n3)/3

if media < 5:
    print('Infelizmente o aluno {} da turma {}, foi reprovado com uma média de de: {}' .format(nome,turma,media))

if media >= 5 and media < 7:
    print('O aluno {}, da turma {}, ficou em recuperação de acordo com a média de: {}' .format(nome,turma,media))

if media > 7:
    print('O aluno {} da turma {}, foi aprovado com uma média de: {}' .format(nome,turma,media))


print ("_" * 80)