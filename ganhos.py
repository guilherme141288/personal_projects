import math

#while loop para nao parar de calcular
while True:
    
    #input para o valor que estava o ativo no momento da compra
    ini = float  (input ('valor comprado: '))
    
    #input para o valor atual
    atu = float (input ('valor atual: '))
    
    #qual o valor que foi investido
    inv = float (input ('de quanto foi o investimento: '))

    resu = (atu - ini)
    resund = (resu / ini) * 100
    rresu = (inv / 100) * resund + inv
    
    #se o valor que estava quando o ativo foi comprado for maior que o valor atual, triga o if
    if ini > atu:
        print ('houve uma queda de {:.2f}%' .format(resund))
        print('o seu investimento de R${} agora vale R${:.2f}, uma queda de R${:.2f}'.format(inv, rresu, (rresu - inv)))
    
    #caso o valor que estava o ativo no momento da compra for menor do que esta atualmente, triga o else
    else:
        print ('o aumento foi de {:.2f}%' .format (resund))
        print ('o seu investimento de R${} agora vale R${:.2f}, um aumento de R${:.2f}' .format(inv , rresu ,(rresu - inv)))