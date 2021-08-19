nome = input("Olá, digite seu nome.")

dia = input("Digite o dia em que você nasceu.")

mes = int(input("Digite o mês em que você nasceu."))

ano = int(input("Digite o ano em que você nasceu."))

idade = 2021 - ano

if (mes > 8): 
    idade = (idade - 1)


print ("Olá {}, sua data de aniversário é: {}/{}/{} e você tem {} anos".format(nome,dia,mes,ano,idade))