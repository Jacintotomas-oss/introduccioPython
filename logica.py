#haremos un cajero automatico 
#listas tiene diferentes tipos de datos en diferentes variable int,string

usuario = list() 
usuario.append("jacino Tomas") # este es string
usuario.append("123456")   # este es string pir el hecho de ser una contraseña
usuario.append(100000) #este es un int por ser el numero de cuenta por eso int

recibo = list()
recibo.append(["1234,600"])
recibo.append(["1235,65"])
recibo.append(["1236,50"])
recibo.append(["1237,700"])

acciones = list()
acciones.append("Depositar")
acciones.append("retirar")
acciones.append("pago de recibo")

usuario2= list()
usuario2.append("chepito")
usuario2.append(1234567)
usuario2.append(10300)

def registrar():
    usuarioRegistrado = list()
    usuarioC = input("ingrese su nombre:")
    usuarioRegistrado=input("ingrese su password:")
    
    #if es selector de flujo
    
    if usuarioC == usuario[0] and usuarioRegistrado== usuario[1]:
    
          print("bienvenido")   
     
    

#si ya hizo el gitt ad y commit puede hacer el push