## Explicação logo depois do código

vel_car = 110
vel_camin = 80

dist_rib_fr = 100

time_car = '{:.2f}'.format(dist_rib_fr / vel_car)

time_car = float(time_car)

tempo_parada_camin = (5 * 2) / 60
tempo_parada_camin = round(tempo_parada_camin)

time_camin = dist_rib_fr / (vel_camin + tempo_parada_camin)

print('O tempo que o carro precisa para cruzar Ribeirão Preto com direção à Franca é {:.2f} horas \n'.format(time_car))

print('O tempo que o caminhão precisa para cruzar Franca com direção à Ribeirão Preto, incluindo atrasos com pedágio é: {:.2f} horas \n'.format(time_camin))

dist_car = vel_car * time_car /2
dist_camin = vel_camin  * time_camin/2

print('A distância percorrida pelo carro até o ponto de encontro é: {:.2f} km \n'.format(dist_car))

print('A distância percorrida pelo caminhão até o ponto de encontro é: {:.2f} km \n'.format(dist_camin))

if dist_car > dist_camin:
    print('O carro chegou primeiro!')
else:
    print('O caminhão chegou primeiro!')
'''
    Explicação: 

    Primeiramente, para a solução do problema temos que ter em mente a fórmula de distancia, aquela mesma que utilizamos principalmente no Ensino Médio em MRU

    Distancia = Velocidade * Tempo

    Só que não temos a variável Tempo, desse modo, temos que calcular o tempo necessário para o carro e o caminhão, respectivamente, cruzarem suas cidades
    e se encontrarem no ponto de encontro

    Para o carro, temos que a velocidade dele é de 110 km/h, e a distância que ele precisa percorrer é de 100 km, desse modo, podemos calcular o tempo

    Tempo = Distancia / Velocidade = 100km / 110km/h 

    Para o caminhão, temos que a velocidade dele é de 80 km/h, e a distância que ele precisa percorrer é de 100 km, desse modo, podemos calcular o tempo


    Entretanto, temos que levar em conta que o caminhão precisa parar para pagar o pedágio, e o tempo que ele precisa parar é de 10 minutos (5 * 2), desse modo, temos que

    Tempo = Distancia / (Velocidade + Tempo de parada) = 100km / (80km/h + 10 min)

    Agora que temos os tempos, podemos calcular a distância percorrida por cada um deles até o ponto de encontro.

    O ponto de encontro seria o local onde ambos se cruzariam.

    O carro, segundo os dados fornecidos estaria ainda em Ribeirão Preto, enquanto o caminhão estaria mais próximo de Franca

'''