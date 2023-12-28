#2.5 minimo, 4h promedio, 7h maximo

#curso dalto 1.5h

#A: cuanta diferencia en % hay entre el curso de dalto, el mas rapido, el mas lento y el promedio

#B: Que % material se redujo del crudo en este caso y en el caso de los otros (crudo promedio es de 5 hs y se convierte en 4hs y el de este curso el crudo es de 3.5hs y se reujo a 1.5hs )

#C: Ver 10 horas de este curso a cuantas horas equivale de los otros cursos? y viceversa?
#--------------------------------------------------

#Promedio de duracion
otros_cursos_min= (2.5)

otros_cursos_prom= (4)

otros_cursos_max= (7)

este_curso= (1.5)

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencia de duracion
diferencia_con_min = 100- este_curso/otros_cursos_min*100

diferencia_con_max = 100- este_curso *1000//otros_cursos_max/10

diferencia_con_prom = 100- este_curso/otros_cursos_prom*100

#Calculando el % de tiempo vacio removido
tiempo_vacio_promedio = 100- otros_cursos_prom *1000//crudo_promedio/10
tiempo_vacio_dalto = 100 - este_curso * 1000// crudo_dalto/10

print (f'Este curso dura un {diferencia_con_min}% menos que el mas rapido')

print (f'Este curso dura un {diferencia_con_max}% menos que el mas lento')

print (f'Este curso dura un {diferencia_con_prom}% menos que el promedio')
print ("-----------------")
#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print (f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print ("-----------------")
#Mostrando dirferencia si los cursos duraran 10 horas
print (f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom * 100// este_curso /10} horas de otros cursos')
print (f'Ver 10 horas de otros cursos equivale a ver {este_curso * 100// otros_cursos_prom / 10} horas de este cursos')
print ("-----------------")