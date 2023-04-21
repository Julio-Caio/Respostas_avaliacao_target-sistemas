# A lista começa com os valores 0 e 1
number1 = 0
number2 = 1

seq_fibonacci = []

seq_fibonacci.append(number1)
seq_fibonacci.append(number2)

number = int(input("Digite um número: "))

while number2 < number:

    prox_num = number1 + number2
    seq_fibonacci.append(prox_num)

    number1, number2 = number2 , prox_num

if number2 == number:
        print(f'O número {number} existe na sequência!')
else:
        print(f'O número {number} não existe na sequência!')

print(f'A sequência de fibonacci é: {seq_fibonacci}')