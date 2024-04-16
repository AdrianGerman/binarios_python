def milti_binaria(binario1, binario2):
    # Convertir los números binarios a enteros y los multiplica
    multiplicacion_decimal = int(binario1, 2) * int(binario2, 2)
    
    # Convertir el resultado de la multiplicación de nuevo a binario y devolverlo
    return bin(multiplicacion_decimal)[2:]


binario1 = input("Ingrese el primer número binario => ")
binario2 = input("Ingrese el segundo número binario => ")

resultado = milti_binaria(binario1, binario2)

print(f"La suma de {binario1} y {binario2} es: {resultado}")
