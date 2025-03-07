#haremos un cajero automatico # trabajo de programacion en clase 
#listas tiene diferentes tipos de datos en diferentes variable int,string

usuario = list() 
usuario.append("jacino Tomas") # este es string
usuario.append("123456")   # este es string pir el hecho de ser una contraseña
usuario.append(100000) #este es un int por ser el numero de cuenta por eso int

recibo = list()
recibo.append(["1234", 600])
recibo.append(["1235", 65])
recibo.append(["1236", 50])
recibo.append(["1237", 700])

acciones = list()
acciones.append("Depositar")
acciones.append("retirar")
acciones.append("pago de recibo")

usuario2= list()
usuario2.append("chepito")
usuario2.append("1234567")
usuario2.append(10300)

def registrar():
    lista = list()
    user = input("ingrese su usuario:")
    password = input("ingrese su contraseña:")

    lista.append(user)
    lista.append(password)
    cuenta = int(input("ingrese su número de cuenta:"))
    lista.append(cuenta)
    if usuario[0] == user and usuario[1] == password:
        print("bienvenido") 
        return lista
    else:
        print("tu usuario o contraseña estan incorrectos")
        oportunidad(lista)

def oportunidad(registro):
    intentos = 0
    while intentos < 3:
        print("intento:", 3 - intentos)
        esValido = registro
        if esValido:
            return esValido
        else:
            intentos += 1

def operacion():
    seleccion = list()
    cantidadOperaciones = ""
    print("seleccione la operacion que desea realizar")
    print("1.Depositar")
    print("2.Retirar")
    print("3.Pago de recibo")
    
    seleccion.append(input("selecciona la operacion que deseas realizar:"))
    
    if seleccion[0] == "1":
        print("depositar")
        cantidadOperaciones = float(input("ingrese la cantidad que desea depositar:"))
        seleccion.append(cantidadOperaciones)
        
    elif seleccion[0] == "2":
        print("retirar")
        cantidadOperaciones = float(input("ingrese la cantidad que desea retirar:"))
        seleccion.append(cantidadOperaciones)  
        
    elif seleccion[0] == "3":
        print("pago de recibo")
        cantidadOperaciones = float(input("ingrese la cantidad que desea pagar:"))
        seleccion.append(cantidadOperaciones)
        
    else:
        print("seleccion invalida")
        
    return seleccion

def retiro(operacion):
    saldo = operacion
    if saldo[1] <= usuario[2]:
        usuario[2] = usuario[2] - saldo[1]
        print("Retiro exitoso")
        print("Saldo actual: ", usuario[2])
        return True
    else:
        print("Cantidad no admitida")
        return False

def deposito(operacion): 
    saldo = operacion()
    if saldo[1] > 0:
        usuario[2] = usuario[2] + saldo[1]
        print("Deposito exitoso")
        print("Saldo actual: ", usuario[2])
    else:
        print("Cantidad no admitida")

def pagoRecibo(operacion):
    op = operacion()
    reciboLista = recibo
    
    for i in range(len(reciboLista)):
        if reciboLista[i][0] == op[1]:
            ingresarMonto = input(
                f"Pago de NIC : {reciboLista[i][0]} , ¿Desea realizar un pago {reciboLista[i][1]} ?  S/N")
            
            if ingresarMonto.lower() == "s":
                if reciboLista[i][1] <= usuario[2]:
                    usuario[2] = usuario[2] - reciboLista[i][1]
                    print("Pago exitoso")
                    print("Saldo actual: ", usuario[2])
                else:
                    print("Saldo insuficiente")
                    return False
        else:
            print("Pago no exitoso")
            print("Saldo actual: ", usuario[2])
            return False
                    
        