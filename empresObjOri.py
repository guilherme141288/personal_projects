class Pessoas:
    
    salario_max = 5000
    ano_atual = 2022
    carga_sem = 40
    
    
    def __init__(self, nome, cpf, idade, posic):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.posic = posic
        print (nome , cpf , idade, posic)
    

    def salario(self):
        
        if self.posic == 'diretor':
            print ('salario: ',self.salario_max)
        if self.posic == 'gerente':
            print ('salario: ',self.salario_max - 1500)   
        if self.posic == 'Zeladora':
            print ('salario: ', self.salario_max - 2500)    

    def anonas(self):
        print ('pessoa nascida em', self.ano_atual - self.idade)

        
instance = Pessoas("joao" , 12457487 , 50 , "diretor")
print(instance.salario())
    





p1 = Pessoas('joao' , '1230485949' , 29 , 'gerente')
p1.salario()
p1.anonas()


p2 = Pessoas('pedro' , '9438439482' , 68 , 'diretor')
p2.salario()
p2.anonas()

p3 = Pessoas('Maria' , '98754854' , 50 , 'Zeladora')
p3.salario()
p3.anonas()

