def suma_binaria(binario1, binario2):
    # Convertir los números binarios a enteros y sumarlos
    suma_decimal = int(binario1, 2) + int(binario2, 2)
    
    # Convertir el resultado de la suma de nuevo a binario y devolverlo
    return bin(suma_decimal)[2:]  # El [2:] es para eliminar el prefijo '0b' que genera la función bin()


# Solicitar los números binarios al usuario
binario1 = input("Ingrese el primer número binario => ")
binario2 = input("Ingrese el segundo número binario => ")

resultado = suma_binaria(binario1, binario2)

print(f"La suma de {binario1} y {binario2} es: {resultado}")
