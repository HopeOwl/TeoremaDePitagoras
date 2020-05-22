def conta():
    resposta = input('Você possui o valor dos dois catetos?(sim/não)\n')
    if resposta == 'sim':
        def conta2():
            try:
                cateto1 = int(input('Informe o valor do primeiro cateto:\n'))
                cateto2 = int(input('Informe o valor do segundo cateto:\n'))
                print(f'O valor da hipotenusa é de: {((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5}')
            except Exception:
                print('Valor incorreto!(Somente números inteiros)')
                conta2()
        conta2()
    elif resposta == 'não':
        def conta3():
            try:
                cateto1 = int(input('Informe o valor do cateto:\n'))
                hipotenusa = int(input('Informe o valor da hipotenusa:\n'))
                print(f'O valor do cateto é de: {((hipotenusa ** 2) - (cateto1 ** 2)) ** 0.5}')
            except Exception:
                print('Valor incorreto!(Somente números inteiros)')
                conta3()
        conta3()
    else:
        print('Resposta inválida!')
        conta()


conta()
while True:
    resposta2 = input('Deseja recomeçar?\n')
    if resposta2 == 'sim':
        conta()
    elif resposta2 == 'não':
        print('Obrigado por usar nosso aplicativo!')
        break
    else:
        print('Resposta inválida!')
