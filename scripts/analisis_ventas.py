#Productos
productos = ["Mouse", "Teclado", "Monitor"`]

#Ventas
ventas = [10, 5, 3]

#Meses
meses = ["Enero", "Febrero", "Marzo"]

#Ventas totales
total = sum(ventas)

#Producto mas vendido
mayor = max(ventas)
indice = ventas.index(mayor)

"Mostrar resultados
print("Ventas totales: ", total)
print("Producto mas vendido: ", producto[indice])

#Ventas por mes
for i in range(len(meses)):
  print(meses[i], ":", ventas[i])
