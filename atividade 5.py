numeros = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

soma = 0
for num in numeros:
    soma += num

print("O total dos números digitados é :", soma)