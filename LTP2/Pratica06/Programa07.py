  
#O programa deve ler o codigo do produto e consultar seu valor em uma
#tabela de precos pre-definida. Exibir o total do pedido para o usuario

def pegarPreco(codigo):
  #Indice == código do produto e conteúdo é igual ao seu valor
  lista_de_precos = [10, 15, 200, 50, 40, 80, 200]
  if codigo >= 0 and codigo < len(lista_de_precos):
    return lista_de_precos[codigo]
  else:
    return -1

def calcularPrecoTotal(lista):
  total = 0
  #Passa por todos os itens da lista
  for item in lista:
    if pegarPreco(item) != -1:
      total = total + pegarPreco(item)
  return total

produtos = []
continuar = True
while continuar:
  codigo = int(input('Codigo:'))
  produtos.append(codigo)
  continuar = input('Continuar?') == 's'
print("Valor Total:", calcularPrecoTotal(produtos))