# preencha uma lista 
 
lista = []
for i in range(10):
    numero = int(input('numero: '))
    lista.append(numero)

print (lista)


# percorrer os itens da lista
cont = 0
for item in lista:
    if item % 2 == 0: 
        cont += 1
print(f'quantidade de numeros pares: {cont}')