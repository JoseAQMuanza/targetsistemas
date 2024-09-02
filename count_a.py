print('-------------------------------------------------')
print('String A/a')
print('-------------------------------------------------')
string = str(input('Digete a string: ').upper())

if string.count('A') != 0:
  print(f'Existem {string.count('A')}')  
else:
  print(f'Na string passada: {string} Não contem a letra A/a')
