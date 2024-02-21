import math

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

#######################################################

def calcula_bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None # Não há solução real

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return (x1, x2)

#######################################################

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

raizes = calcula_bhaskara(a, b, c)

if raizes is None:
    print("A equação não tem solução real.")
else:
    print(f"As raízes da equação são: {raizes[0]:.2f} e {raizes[1]:.2f}")

#######################################################

L = []
for x in range(10,1,-2):
  L.append(x)
  print(L[2:4])


#######################################################
  

letras = ["P", "F"]
for x in letras:
  {
    print(x)
  }

#######################################################

def fatorial(numero)->list :
  if numero == 0 or numero == 1:
    return 1
  else:
      return numero * fatorial(numero-1)

x = int(input("Digite um número:"))
fatorial = fatorial(x)
print(f"O fatorial de {x} é {fatorial}")

#######################################################

def funcao(x):
    if x <= 1:
        return 1
    else:
        return x + (funcao(x - 1) * funcao(x - 2))

print(funcao(4))