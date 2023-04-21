### questao A)

for i in range(1, 10, 2):
    print(i, end=' ')

print()


### Questão B)

binarios = 2
seq = []

for i in range(1, 129):
    seq_bin = binarios ** i
    seq.append(seq_bin)

    if seq_bin >= 128:
        break

print(seq)

### questao C)

lista = []
sum = 0

for i in range(0, 49):
    if i % 2 != 0:
       sum += (1 * i)
       lista.append(sum)
    
    if sum >= 49:
           break

print(lista)


### questao D)

quad_perf = []

for i in range(2, 93):
    if i % 2 ==0:
        num = i ** 2
        quad_perf.append(num)

    if num >= 93:
        break
print(quad_perf)

### questao E)

number1 = 0
number2 = 1

seq_fibonacci = []

seq_fibonacci.append(number1)
seq_fibonacci.append(number2)

for i in range(0, 14):
    prox_num = number1 + number2
    seq_fibonacci.append(prox_num)

    number1, number2 = number2 , prox_num

    if prox_num >= 13:
        break

print(seq_fibonacci)