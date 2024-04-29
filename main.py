a=5
b=10
print("Hola mundo")
print("La suma es: ", a+b)
print("La resta es: ", a-b)
print("*****************************")
print("********CALCULADORA**********")
print("*****************************")
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
print("Calculadora")
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
print("Elige la operación:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (x)")
print("4. División (/)")
opcion = input("Ingresa el número de la operación deseada: ")
if opcion == '1':
    print("El resultado de la suma es:", suma(numero1, numero2))
elif opcion == '2':
    print("El resultado de la resta es:", resta(numero1, numero2))
elif opcion == '3':
    print("El resultado de la multiplicación es:", multiplicacion(numero1, numero2))
elif opcion == '4':
    print("El resultado de la división es:", division(numero1, numero2))
else:
    print("Opción no válida")
