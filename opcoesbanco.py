#programa usado pelo funcionario para aprovação ou nao de algum tipo de transação

print ('''Qual serviço o cliente deseja: 

[ 1 ] Emprestimo pessoal
[ 2 ] financialmento de imovel
[ 3 ] Financiamento de veiculo''')

var_01 = int(input('sua opção: '))

if var_01 == 1:
    #coletando dados para calculo
    var_02 = int(input('Qual o valor do emprestimo: '))
    var_03 = int(input('Em quantos meses ele ira pagar: '))
    var_07 = int(input('Salario mensal do contratante: '))
    var_04 = bool(input('Tem nome sujo no serasa?(nao digite nada caso não tenha) '))
    
    #calculando 20% do salario
    var_05 = var_07 / 100 * 20
    print (var_05)

    #calculando valor da parcela, com 2% de juros do valor total
    var_06 = (var_02 + (var_02 / 100 * 2)) / var_03   

    
    
    if var_06 > var_05 and var_04 is True:
        print (f'''Para pagar um emprestimo de R${var_02} em {var_03} meses, a parcela será de R${var_06:.2f}
        Imprestimo nao concedido pois o cliente já tem pendencias a pagar''')
    elif var_06 > var_05 and var_04 is False:
        print (f'''Para pagar um emprestimo de R${var_02} em {var_03} meses, a parcela será de R${var_06:.2f}
        Imprestimo nâo pode ser concedido, Parcela acima do que o cliente pode pagar''')
    elif var_05 > var_06 and var_04 is True:
        print (f'''Para pagar um emprestimo de R${var_02} em {var_03} meses, a parcela será de R${var_06:.2f}
        Imprestimo concedido, porém somente após limpar o nome do serasa''')    
    elif var_05 > var_06 and var_04 is False:
        print (f'''Para pagar um emprestimo de R${var_02} em {var_03} meses, a parcela será de R${var_06:.2f}
        Imprestimo concedido para retirada imediata ''')




