p=open('archivo.txt','w')
lista = [
    'uno',
    'dos',
    'tres', 'viva','el pollo'
]
for linea in lista:
    if not linea.endswith('\n'):
      linea = linea + '\n'
    p.write(linea)
p.close()