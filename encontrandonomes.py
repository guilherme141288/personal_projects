#identificando primeira e ultima letra/palavra/text


nome_procurado = str(input('Digite o primeiro nome da pessoa a ser procurada: ')).upper()
#print (nome_procurado)


lista_nomes1 = str(input('coloque a lista de nomes aqui: ')).upper()


#var_01 = input('Digite seu nome completo: ').split().upper()

#print (var_01)


if nome_procurado in lista_nomes1 :
    lista_nomes = [nome_procurado]
    
    #lista_nomes.append(lista_nomes)
    #lista_nomes.count(lista_nomes)


  
    
    print (lista_nomes)
else:
    print('nenhum encontrado')    


