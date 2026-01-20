import math

def suma_numeros():
    n = int(input("Cantidad de números: "))
    total = 0
    for i in range(n):
        total += float(input(f"Número {i+1}: "))
    print("Suma:", total)

def producto_numeros():
    n = int(input("Cantidad de números: "))
    resultado = 1
    for i in range(n):
        resultado *= float(input(f"Número {i+1}: "))
    print("Producto:", resultado)

def division():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    if b == 0:
        print("Error: división entre cero")
    else:
        print("Resultado:", a / b)

def factorial():
    n = int(input("Ingrese un número: "))
    if n < 0:
        print("No existe factorial de negativos")
    else:
        print("Factorial:", math.factorial(n))

def tabla_multiplicar():
    n = int(input("Número de la tabla (1–10): "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def cuadrado_cubo():
    n = float(input("Ingrese un número: "))
    print("Cuadrado:", n**2)
    print("Cubo:", n**3)

while True:
    print("\nMENÚ")
    print("1. Suma")
    print("2. Producto")
    print("3. División")
    print("4. Factorial")
    print("5. Tabla de multiplicar")
    print("6. Cuadrado y cubo")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        suma_numeros()
    elif opcion == "2":
        producto_numeros()
    elif opcion == "3":
        division()
    elif opcion == "4":
        factorial()
    elif opcion == "5":
        tabla_multiplicar()
    elif opcion == "6":
        cuadrado_cubo()
    elif opcion == "7":
        break
    else:
        print("Opción inválida")
