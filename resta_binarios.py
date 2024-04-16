def resta_binaria(binario1, binario2):
    # Convertir los números binarios a enteros
    num1 = int(binario1, 2)
    num2 = int(binario2, 2)
    
    # Realizar la resta
    resta_decimal = num1 - num2
    
    # Manejar el caso de que la resta resulte en un número negativo
    if resta_decimal < 0:
        raise ValueError("La resta de binarios resulta en un número negativo.")
    
    # Convertir el resultado de la resta de nuevo a binario y devolverlo
    return bin(resta_decimal)[2:].zfill(max(len(binario1), len(binario2)))  # zfill() para asegurar que tenga la misma longitud


binario1 = input("Ingrese el primer número binario: ")
binario2 = input("Ingrese el segundo número binario: ")

# Realizar la resta de los números binarios
try:
    resultado = resta_binaria(binario1, binario2)
    print(f"La resta de {binario1} y {binario2} es: {resultado}")
except ValueError as e:
    print("Error:", e)
