mi_diccionario = {
    'nombre': 'Fede',
    'edad': 30,
    'ciudad': 'Morenegro'
}

print(mi_diccionario['nombre']) #Salida: 'Fede'


#MODIFICAR EL VALOR DE 'EDAD'
mi_diccionario['edad'] =31


#AGREGAR NUEVA INFORMACION
mi_diccionario['profesion'] = 'Desarrollador'


#RECORRER EL DICCIONARIO
for clave, valor in mi_diccionario.items():
    print(f'{clave}: {valor}')