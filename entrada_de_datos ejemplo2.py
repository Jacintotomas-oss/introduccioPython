import math 
def calcularInteres (precio,interes):
    return precio* interes

def calcularPrecio (precio, ganancia):
    return precio + (ganancia*precio)

def precioVenta (precio, interes, ganancia):
    total = calcularPrecio(precio, ganancia)
    interes= calcularInteres
    
    return total + interes

interes = float(input("Ingrese el interes: "))
ganancia = float(input("Ingrese la ganancia: "))
precio = float(input("Ingrese el precio: "))

print(precioVenta(precio, interes, ganancia))

def calculadora():
    print ("calculadora basica") 
    print("selecciona una operacion")
    print("1.- suma")
    print("2.- resta")
    print("3.- multiplicacion")
    print("4.- division")
    print("5.- salir")
    
    opcion = input("ingrese la operacion que desea realizar:")
    
    if opcion in ("1","2","3","4"):
        num1 = float(input("ingrese el primer numero:"))
        num2 = float(input("ingrese el segundo numero:"))
        
        if opcion == "1": 
            print(f"el resultado de {num1} + {num2}= {num1+num2}")
        elif opcion == "2":
            print(f"el resultado de {num1} - {num2} ={num1-num2} ")
    elif opcion == "3":
        print(f"el resultado de {num1} * {num2} = {num1*num2}")
    elif opcion =="4":
        
        if num2 == 0:
             print(f"el resultado de {num1} / {num2} = {num1/num2}")
        else:
            print("no se puede dividir entre 0")
    else: 
        print("opcion invalida intenteo denuevo")
        
        calculadora()
        
        import random
        
        def numero_aleatorio():
            print("generador de numeros aleatorios")
            num = random.randint(1, 100)
            print(f"es el numero generado: {num}")
            
            numero_aleatorio()
            
            def comparar_cadenas():
                cadena1 = input("ingrese la primera cadena:")
                cadena2 = input("ingrese la segunda cadena:")
                
                if  cadena1 == cadena2:
                    print("las cadenas son iguales")
                else:
                    print("las cadenas son diferentes")
                    if cadena1 > cadena2:
                        print(f"{cadena1}es mayor en orden alfabetico que {cadena2}")
                        print(f"{cadena2}es mayor en orden alfabetico que {cadena1}")
                        
                        comparar_cadenas()
                        
                        print("bienvenido dinos el precio,ganancia y impuesto")
                        
precio =(input("ingrese el precio:"))
precio = float(precio)
ganancia =(input("ingrese la ganacia:"))
ganancia = float(ganancia)
impuesto =(input("ingrese el impuesto:"))
impuesto = float(impuesto)
 
def calcularImpuesto(precio, impuesto):
    return precio * impuesto
def calcularGanancia(ganancia, precio):
    return precio * ganancia

def calcularPrecioFinal(precio, impuesto, ganancia):
    precio1 = calcularGanancia(ganancia, precio) + precio
    impuestVenta = calcularImpuesto(impuesto, precio1)
    return precio1 + impuestVenta

print(calcularPrecioFinal(precio, impuesto, ganancia))