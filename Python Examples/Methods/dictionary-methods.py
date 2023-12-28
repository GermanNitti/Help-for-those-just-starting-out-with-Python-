diccionario = {
    "nombre": "German",
        "apellido": "Ruiz",
            "edad": "31"
}

#nos devuelve 
claves = diccionario.keys()
#obteniendo un elemento con get() (si no encuentra nada el programa continua) :)
valor_de_asgasgs = diccionario.get("asgasgs")
print("Si, funciona tranqui")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
#-diccionario.pop("apellido","edad") #suplanta el primer valor por el ultimo valor
#-print(diccionario)
#para eliminar mas de un valor, se debe utilizar un bucle for
claves_a_eliminar = ["apellido", "nombre"]

for clave in claves_a_eliminar:
    diccionario.pop(clave, None)

print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)


