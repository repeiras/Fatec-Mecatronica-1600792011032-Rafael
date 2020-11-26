console = {"xbox_s": [] , "xbox_x": [], "ps5": []}

continuar = True
while continuar == True:
  classe = input("Qual console:").lower()
  if classe in console.keys():
    console[classe].append(console)
    #Avança para o próximo registro
  contador += 1
  else:
    print("Console invalida!")
print(console)
continuar = input("Continuar?").lower() == 's'

print("Porcentagens Relativas:")
for categoria in console.keys():
  porcentagem = len(console[categoria])/quantidade_de_personagens
  print("Categoria:", categoria, " - ", porcentagem * 100)

print("console:")
for categoria in console.keys():
  print("Console:", categoria.capitalize())
  for nome_de_console in console[categoria]:
    print(console)
  print('-------')
