#ESTO ESTA PARA QUE FUNCIONEN ALGUNOS EJEMPLOS
cadena1 = "Hola soy German"
cadena2 = "Bienvenido lince"


#HAY ALGUNAS FUNCIONES Y UNOS METODOS
#function(cadena)
#cadena.metodo()
#----------------------------

# 'upper()' Convierte todos los caracteres de la cadena a mayúsculas.

texto = "Hola, Mundo!"
print(texto.upper())  # Output: HOLA, MUNDO!

#-----------------------------


# 'lower()' Convierte todos los caracteres de la cadena a minúsculas.

texto = "Hola, Mundo!"
print(texto.lower())  # Output: hola, mundo!

#-----------------------------


# 'capitalize()' Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas.

texto = "hola, mundo!"
print(texto.capitalize())  # Output: Hola, mundo!

#-----------------------------


# 'title()' Convierte la primera letra de cada palabra a mayúscula.

texto = "hola, mundo!"
print(texto.title())  # Output: Hola, Mundo!

#-------------------------


# 'len()' Devuelve la longitud de la cadena (número de caracteres).

cadena = "Hola, mundo!"
print(len(cadena))  # Output: 13

#-------------------------


#'strip()' Elimina espacios en blanco (u otros caracteres especificados) del principio y el final de la cadena.

texto = "   Hola, Mundo!   "
print(texto.strip())  # Output: Hola, Mundo!

#-------------------------


#'replace()' Reemplaza una subcadena con otra subcadena.

texto = "Hola, Mundo!"
nuevo_texto = texto.replace("Mundo", "Python")
print(nuevo_texto)  # Output: Hola, Python!

#--------------------------


#'split()' Divide la cadena en una lista de subcadenas según un delimitador.

texto = "Hola, Mundo!"
palabras = texto.split(", ")
print(palabras)  # Output: ['Hola', 'Mundo!']


#'find()' Buscamos una cadena con otra cadena. (si no hay coincidencias devuelve -1).

busqueda_find = cadena1.find ("G")
print(busqueda_find) #Output: ['9']

#---------------------------


#'index()' Buscamos una cadena con otra cadena. (En este caso si no hay coincidencia, nos da una excepcion).

busqueda_index = cadena1.index("G")
print (busqueda_index) #Output: ['9']

#----------------------------


#'isnumeric()' Si es numerico, devuelve True, sino False.

es_numerico = cadena1.isnumeric()
print(es_numerico) #Output: [T o F]

#------------------------------


#'isalpha()' Si es alfa numerico devuelve True, sino False. (solo funciona con caracteres de la A a la Z y numeros).

es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico) #Output: [T o F]

#-------------------------------


#'count()' Buscamos una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida.

contar_coincidencias = cadena2.count("n")
print(contar_coincidencias) #Output: [3]

#--------------------------------


#'startswith()' Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True.
empieza_con = cadena1.startswith("H")
print (empieza_con) #Output: [True]

#----------------------------------


#'endswith()' Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True.
termina_con = cadena1.endswith("n")
print (termina_con) #Output: [True]

