numeros = []
np = 0

while True:
    num = int(input('Digite um número inteiro: '))
    if num ==0:
        break

    numeros.append(num)
    if num % 2 == 0:
        np = np + 1

if numeros:
    print('A soma dos números é ',sum(numeros))
    print('O maior número é ',max(numeros))
    print('O menor número é ',min(numeros))
    print(F'A quantidade de números pares são {np}')
else:
    print('Nenhum número foi digitado')