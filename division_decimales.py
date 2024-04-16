def division_binaria(dividendo, divisor):
    # convertir los números binarios a enteros
    num1 = int(dividendo, 2)
    num2 = int(divisor, 2)
    
    # manejar el caso de que la división de 0
    if num2 == 0:
        raise ValueError('¡Error! División por cero.')
    
    # realizando la división
    cociente_decimal = num1 // num2
    residuo_decimal = num1 % num2
    
    # convertir los resultados de nuevo a binarios
    cociente_binario = bin(cociente_decimal)[2:]
    residuo_binario = bin(residuo_decimal)[2:]
    
    return cociente_binario, residuo_binario

# solicitar los números

dividendo = input('Ingresa el dividendo binario => ')
divisor = input('Ingresa el divisor binario => ')

# realiza la división

try: 
    cociente, residuo = division_binaria(dividendo, divisor)
    print(f"El cociente de la división es: {cociente}")
    print(f"El residuo de la división es: {residuo}")
except ValueError as e:
    print("Error:", e)
