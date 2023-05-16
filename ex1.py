pares = []
impares = []


for n in range(10):
    numero = int(input('numeros: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)