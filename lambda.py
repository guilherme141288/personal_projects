valor = (int(input('Valor do produto: ')))

calcular_desconto = lambda valor : valor * 0.24

print (f'O valor do produto com 24% de desconto fica {calcular_desconto(valor - calcular_desconto)}')