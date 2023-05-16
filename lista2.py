def busca(lista, item):
    for n in lista:
        if n == item:
            return True
    return False

lista = []
while True:
    n = int(input('informe um numero inteiro: '))
    if n == 0:
        break
    lista.append(n)
print(lista)


item = int(input('informe um numero para buscar na lista: '))
if busca(lista, item):
    print('o numero está contido na lista')
else:
    print(f'o numero {item} não está contido na lista')