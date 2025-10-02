banco_d = {
'nomes':['Ana','Jose'],
'login':{
    '@ana':'1',
    '@jose':'2'
},
'notas':
{
'julia':[],
'caio':[]

}
}

print('SISTEMA DE LANÇAMENTO DE NOTAS ESCOLAR Z')
tentativas  =  3
while tentativas > 0:
    login_usu = input('Login: ')
    senha_usu = input('Senha: ')
    tentativas -= 1
    if login_usu in banco_d['login'] and senha_usu == banco_d['login'][login_usu]:
       print('SEJA BEM VINDO(A) AO SISTEMA Z DE NOTAS')
       
       resposta =  input('Deseja cadastrar? ')
       while resposta == 'sim':
            quantidade_notas = int(input('Quantidade de notas: '))
            for n in range(quantidade_notas):
                nome = input('Nome:')
                nota = float(input('Nota: '))
                banco_d['notas'][nome].append(nota)
                print(nome)
                media  =  sum(banco_d['notas'][nome])/len(banco_d['notas'][nome])
                print('media:', media)
            resposta = input('Deseja cadastra as notas de outro aluno?')
           
       else:
             print('saindo do SISTEMA...')


    else:
        print(f'Você tem apenas {tentativas} tentativas')
else:        
    print('CONTA BLOQUEADA ENTRE EM CONTATO COM O SUPORTE')        

input('Deseja sair do sistema, clique enter?')


# executavel  
      