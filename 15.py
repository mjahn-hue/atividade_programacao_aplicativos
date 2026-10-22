numero = int(input("Digite um número: "))
i = 0
while numero != 0:
    if numero > 0:
        i += 1
    numero = int(input("Digite um número: "))


print("A quantidade de números positivos digitados é: ", i)