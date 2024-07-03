#9
nombreApellido = input("cual es su nombre y apellido?")
programacion1 = int(input("Que nota tenes en el primer cuatrimestre?"))
prog2 = int(input("en el segundo?"))
prog3 = int(input("en el tercero?"))
promedio = (programacion1 + prog2 + prog3) // 3
print("El alumno " + nombreApellido + "tiene un promedio de " + 
      str(promedio))