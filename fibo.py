print('-------------------------------------------------')
print('Sequência de Fibonacci')
print('-------------------------------------------------')
term = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1
fib = ['0', '1']
c = 3
while c <= 100:
    if len(fib) == 0:
        pass
    else:
        t3 = t1 + t2
        fib.append(t3)        
        t1 = t2
        t2 = t3
        c += 1


for n in fib:
    print(f'-> {n} ', end='')
if fib.count(int(term)):
    print('\nO termo existem dentro da sequencia!')
    print('FIM')    
else:
    print('\nO termo não existem dentro da sequencia!')
    print(fib.count(term))
    print('FIM')    