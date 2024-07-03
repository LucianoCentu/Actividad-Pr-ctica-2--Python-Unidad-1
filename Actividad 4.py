#4
print("Dime tu nombre")
nombre = input()
print("Dime tu numero de comision")
comision = input()
#Para simplificar codigo puse la pregunta del print en los parentecis del input
asignatura = input("Dime la asignatura")
docente = input("Dime el nombre del docente")
presente = input("El usuario esta presente?")
print( nombre + " de la comision " + comision + " de "
      + asignatura + " con el docente " + docente + "."
     + presente + " estuvo presente.")