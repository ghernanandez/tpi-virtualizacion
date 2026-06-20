print("----CONVERTOR DE DECIMAL A BINARIO----")

# 1. Inicializar lista vacía
binario = []

# 2. Solicitar datos al usuario
numero = int(input("Ingrese un número decimal: "))
n = numero

# 3. Calcular el binario
if n == 0:
    binario.append(0)
else:
    while n > 0:
        binario.append(n % 2)
        n = n // 2
    binario.reverse()

# 4. Mostrar resultado
resultado = "".join(str(bit) for bit in binario)
print(f"El número {numero} en binario es: {resultado}")