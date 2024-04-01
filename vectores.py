vector = []
for i in range(6):
    try:
        num = int(input("Ingrese un números: "))
        vector.append(num)
    except ValueError:
        print("Error: Ingrese un número válido.")
        

print("Los números ingresados son:", vector)

vector_multiplos = []

try:
    for i in vector:
        if i % 2 == 0:
            vector_multiplos.append(i)
    print("Los múltiplos de dos son:", vector_multiplos)
except:
    print("Error: No hay números múltiplos de 2.")

    




