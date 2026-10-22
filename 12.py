numero = int(input("Digite um número: "))
numero_soma = 0
while numero != 0:
    numero_soma += numero
    numero = int(input("Digite um número: "))

print("A soma dos números digitados é: ", numero_soma)