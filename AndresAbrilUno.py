print('Promediador de notas estudiantiles')
print('Dicte sus notas y si quiere cerrar el programa ponga "salir"')
notas=[]
while True:
  x=int(input('>>'))
  if x == 'salir':
    break
  else:
    notas.append(x)
resultado=0
for nota in notas:
  resultado+=nota
print(f'tu promedio es de {resultado/(len(notas))}')
