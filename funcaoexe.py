def layout():

    print('nao pode passar, pois o nome nao esta na lista')

ESCOLHIDOS = ['joao' , 'ricardo' , 'pedro' , 'henrique']


var_01 = input('seu nome?')

print(f'Bom dia {var_01}')

if var_01 in ESCOLHIDOS:
    print ('pode passar')
else:
    layout()    