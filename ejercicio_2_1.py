import numpy as np

# Se Define un array de cuatro dimensiones, en este caso se eligió numeros entre 1 y 20.
#(2, 3, 4, 5) Estas 4 dimensiones implican que el array tiene 2 matrices tridimensional, 
#cada una con 3 filas, 4 columnas y 5 elementos en cada celda.
array_4d = np.random.randint(1, 10, size=(2, 3, 4, 5))

# Mostrar las dimensiones del array
print("Dimensiones del array :")
print(array_4d.shape)
# Mostrar el Numero de dimensiones del array
print("es un array de : ",array_4d.ndim," dimensiones")

# Mostrar el contenido del array
print("\nContenido del array de cuatro dimensiones:")
print(array_4d)

# Calcular la suma de los elementos en función de los dos últimos ejes
suma_por_2_ultimos = np.sum(array_4d, axis=(-2, -1))
# Mostrar resultado de la suma
print("\nSuma de los elementos en función de los dos últimos ejes:")
print(suma_por_2_ultimos)
