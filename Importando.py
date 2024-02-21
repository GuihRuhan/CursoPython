import random
import math

A1 = int(input('primeiro algulo: '))
A2 = int(input('Segundo angulo: '))
A3= int(input('Terceiro angulo: '))

if (0 < A1 < 90) and (0 < A2 < 90) and (0 < A3 < 90) :
  print('Você tem um triangulo acutângulo :) ')
if A1 + A2 + A3 == 180 :
  print('Você tem um triangulo retângulo ;)')

####################################################################
  
#Entrada
Salario = int(input('Informe seu salário: '))
tempotrabalhado = int(input('Informe seu tempo trabalhado: '))

if  10 > tempotrabalhado:
     print(f'Seu bônus será de {Salario * 0.10 } R$')
if 6> tempotrabalhado < 10:
     print(f'Seu bônus será de {Salario * 0.08 } R$')
if tempotrabalhado < 6:
      print(f'Seu bônus será de {Salario * 0.05 } R$')

####################################################################

x = int(input('digite o primeiro número:'))
y = int(input('digite o segundo número:'))
operacao = input('digite a operação: *, +, -, /:')
if operacao == '*':
  print(x*y)
elif operacao == '/':
  print(x/y)
elif operacao == '+':
  print(x+y)
elif operacao == '-':
  print(x-y)

####################################################################

opcoes = ['papel', 'pedra', 'tesoura']

escolha_computador = random.choice(opcoes)

escolha_computador

####################################################################

import random

opcoes = ['papel', 'pedra', 'tesoura']

escolha_computador = random.choice(opcoes)

escolha_usuario = input('Faça sua escolha pedra, papel, tesoura:')

if escolha_computador == 'pedra' and escolha_usuario == 'tesoura':
 print(f'Computador venceu:{escolha_computador}')
elif escolha_computador =='tesoura' and escolha_usuario =='papel':
  print(f'Computador venceu:{escolha_computador}')
elif escolha_computador =='papel' and escolha_usuario == 'pedra':
  print(f'Computador venceu:{escolha_computador}')
elif escolha_computador == escolha_usuario:
  print('Empate')
else:
  print(f'você venceu:{escolha_computador}')

####################################################################


#para calcular raiz quadrada, usa-se apenas **0.5

a= int(input('Insira o valor: '))
b= int(input('Insira o valor: '))
c= int(input('Insira o valor: '))
delta = b**2 - 4*a*c

if delta < 0:
  print('Não existe raiz') # Não há solução real
else:
  x1 = (-b + (delta)**5) / (2*a)
  x2 = (-b - (delta))**5 / (2*a)
  print( x1, x2)


####################################################################


def calcula_bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None # Não há solução real

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return (x1, x2)

####################################################################


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

raizes = calcula_bhaskara(a, b, c)

if raizes is None:
    print("A equação não tem solução real.")
else:
    print(f"As raízes da equação são: {raizes[0]:.2f} e {raizes[1]:.2f}")