
operações = input('Qual operação você deseja fazer?')
if operações == ('sum') or ('addition') or ('+'):
    n1 = float(input('Tell me a number to sum'))
    n2 = float(input('Tell me a number to complete the addition'))
    resultado = n1 + n2   
    result_soma = print('The result of this addition is:', resultado)

if operações == ('division') or ('/') or (':'):
    nd1 = float(input('Tell me a number to divide'))
    nd2 = float(input('Tell me the divider'))
    result_d = nd1/nd2
    result_divisão = print('The result of this division is:', result_d)

if operações == ('multiplication')or ('*') or ('.'):
        nm1 = float(input('Give me a number to multiply'))
        nm2 = float(input('Tell me the multiplicator of this number'))
        result_m = nm1*nm2
        result_multiplicação = print('The result of this multiplication is:', result_m)

if operações == ('subtration') or ('-'):
     ns1 = float(input('Tell me a number to subtract'))
     ns2 = float(input('Tell me the number that will subtract the earlier number'))
     result_s = ns1-ns2
     result_sub = print('The result of this subtration is:', result_s)

else:
     print('Unknown operation')
