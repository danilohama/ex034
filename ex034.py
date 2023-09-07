"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
> Para salários superiores a R$1250,00 calcule um aumento de 10%.
> Para os inferiores ou iguais, o aumento é de 15%"""
salario = float(input('Qual é o salario do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O funcionário que ganhava R$\33[0:31m{:.2f}\33[0:m passa a ganhar R$\33[0:32m{:.2f}\33[0:0m agora'
      .format(salario, novo))
