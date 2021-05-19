print('calculadora')

#Entrada dos valores
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#Entrada da informação desejada
operacao = input('Digite a operacao desejada *em minusculo e sem caracteres especiais: ')

#calcula adicao
if operacao == 'adicao':
    resultado = num1 + num2
    print('A soma dos dois números é : ',resultado)

#calcula subtracao
elif operacao == 'subtracao':
    resultado = num1 - num2
    print('A diferença dos dois números é : ',resultado)
    
#calcula divisao 
elif operacao == 'divisao':
    resultado = float(num1 / num2)
    print('A divisão do primeiro número pelo segundo resultou em: ', resultado)
    
#calcula multiplicacao
elif operacao == 'multiplicacao':
    resultado = num1 * num2
    print('O resultado da multiplicação é: ', resultado)
