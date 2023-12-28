#Creando una lista con list()
lista = list(["hola", "ger",24, 12, 23, True])


#Devuelve la cantidad de elementos de la lista
resultado = len(lista)
print(resultado)#Output: [6]

#agregando un elemento a la lista
agregando_con_append = lista.append("jajajaja") #aca le estamos agregando un elemento a la lista
print(agregando_con_append) #Output: ["hola", "ger", 24, 12, 23, True, "jajajaja"]

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "ñangale")
print(lista) #Output: ["hola", "ger", "ñangale", 24, 12, 23, True]

#agregando varios elementos a la lista
lista.extend([False,2030]) #en cambio aca le estamos agregando una lista a la lista (esta entre [])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente.

#removiendo un elemento de la lista por su valor
lista.remove("ñangale")
print(lista)

#aliminando todos los elementos de la lista
lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro revers=True lo ordena en reversa)
lista.sort() #No funciona si tiene strings ("hola soy un string")

#invirtiendo los elementos de una lista
lista.reverse()
print (lista)

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(12)

#SE PUEDE UTILIZAR 'dir' PARA OBTENER UNA LISTA DE ATRIBUTOS Y METODOS QUE SE PUEDAN USAR (EJEMPLO)

mi_lista = [1, 2, 3]
print(dir(mi_lista))#esto nos va a devolver algo como: append(), clear(), count(), extend(), insert(), remove(), reverse(), sort(), ETC....
