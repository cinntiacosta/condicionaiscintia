#Condicionais

print("Digite a primeira nota: ")
n1 = float(input())

print("Digite a segunda nota 2: ")
n2 = float(input())

media = (n1 + n2) / 2
print("Média = ", media)

if media >= 7.0:
  print("Aprovado (a)!")
elif media < 7.0:
  print("Exame!")
  print("Digite a nota do exame: ")
  n3 = float(input())
  exame = (media + n3) / 2
  if exame >= 6.0:
    print("Média final = ", exame)
    print("Aprovado(a)!")
  else:
    print("Média final = ", exame)
    print("Reprovado(a)!")