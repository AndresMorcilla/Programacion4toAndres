print('Promediador de notas estudiantiles')
print('Dicte sus notas y si quiere cerrar el programa ponga "salir"')
notas=[]
while True:
  x=input('>>')
  if x == 'salir':
    break
  else:
    notas.append(int(x))
resultado=0
for nota in notas:
  resultado+=nota
print(f'tu promedio es de {resultado/(len(notas))}')
