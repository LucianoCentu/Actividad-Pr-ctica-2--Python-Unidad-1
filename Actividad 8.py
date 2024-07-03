#8
producto = input("Cual es el producto")
precio = int(input("Cual es el precio"))
iva = (precio * 0.21)
total = (precio + (precio * 0.21))
print(" el IVA es de " + str(iva))
print("el total con el IVA es de " + str(total))
