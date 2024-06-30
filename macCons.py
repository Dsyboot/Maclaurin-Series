# Importar la libreria de funciones
from functions import InvalidCommandException, Math, Solver
from os import system
from datetime import datetime
from time import sleep
import platform as plt

# Obtener la fecha en que se abre el programa
prstart = datetime.now().strftime("%d:%m:%Y %H:%M:%S")

# Variable global para almacenar el historial
expressions_history = [] # (time, expr, result, grados, range)
global_result = "" # Ultima respuesta
ans = 0.0 # Ultima respuesta

# Funcion para limpiar la pantalla
def cleardevice():
    if plt.system().lower() in "windows":
        system("cls")
    else:
        system("clear")
    #end if
#end def

# Funcion para obtener un comando
def operation() -> int:
    # Pedirle al usuario un valor
    funct = input("Evaluar: ")
    
    # Formatear el input para devolver un comando
    funct = funct.strip()
    
    if any(comando in funct for comando in ["/save", "/range", "/chgrad", "/exit"]):
        # Es un comando, se necesita devolver
        if funct == "/save":
            return 0
        elif funct == "/chgrad":
            return 1
        elif funct == "/exit":
            return 2
        #end if
        
        # Comando especial, se evalua en este lugar
        if "/range" in funct:
            try:
                # Formatear a int el valor
                value = int(funct.replace("/range", "").strip())
                
                Math.intensity(value) # Establecer el valor de n
            except:
                raise InvalidCommandException("El valor de n debe ser un entero!")
            #end try
        #end if
    else:
        # No es un comando, asi que se evalua la expresion
        solve = Solver() # Crear objeto de la clase Solver
        global ans
        solve.functions["ans"] = ans
        
        # Eliminar el rastro de los comandos
        funct = funct.lower().replace("/save", "").replace("/chgrad", "").replace("/exit", "")
        
        # Cambiar el signo por texto
        funct = funct.replace("π", "pi").replace("τ", "tau").replace("∞", "inf")
        result, error = solve.evaluate_expression(funct)
        result = str(result).replace("inf", "∞").replace("nan", "Forma Indeterminada")
        
        # Imprimir el resultado
        if not error:
            global expressions_history
            
            try:
                ans = float(result)
                solve.functions["ans"] = ans
            except:
                ans = ans
            #end try
            
            # Guardar en el historial
            now = datetime.now().strftime("%d:%m:%Y %H:%M:%S")
            expressions_history.append((now, funct, result, str("Radianes" if Math.inRadians else "Grados"), Math.n))
        #end if
        
        global global_result
        global_result = f"Resultado: {result}\n"
    #end if
    
    return -1
#end def

# Funcion para guardar un log en la computadora
def save_log():
    global expressions_history
    
    if len(expressions_history) > 0:
        with open("history.txt", "a") as data:
            data.write("-"*80)
            data.write(f"\nProgram openned: {prstart}\n")
            data.write("-"*80)
            
            # Intentar guardar los datos al archivo
            try:
                for index, vals in enumerate(expressions_history):
                    hora, func, result, grType, nVal = vals
                    data.write(f"\nEcuacion: #{index + 1}\n")
                    data.write(f"Realizada con: {grType}\n")
                    data.write(f"Valor de n: {nVal}\n")
                    data.write(f"Hora de ejecucion: {hora}\n")
                    data.write(f"Funcion ingresada: {func}\n")
                    data.write(f"Resultado: {result}\n")
                #end for
            except:
                pass
            #end try
            
            data.write(("-"*80) + "\n\n")
            data.close()
        #end with
        
        # Reiniciar los valores guardados
        expressions_history = []
        
        # Simplemente un mensaje
        print("Guardando...")
        sleep(1.25)
        print("Exito!")
        sleep(0.5)
    #end if
#end def

# Funcion para correr el programa
def run(): 
    global global_result
    
    while True:
        # Borrar pantalla y mostrar el titulo
        cleardevice()
        print(f"Series de maclaurin (n = {Math.n}) (En: {'Radianes' if Math.inRadians else 'Grados'})\n")
        
        # Mostrar las ecuaciones y sus restricciones
        print("-"*50)
        print("Ecuaciones disponibles:")
        print("fact(x)       x es Natural")
        print("sin(x)        x es Real")
        print("cos(x)        x es Real")
        print("arcsin(x)     -1 ≤ x ≤ 1")
        print("arccos(x)     -1 ≤ x ≤ 1")
        print("arctan(x)     x es Real")
        print("exp(x)        x es Real")
        print("ln(1 + x)     x > 0")
        print("sinh(x)       x es Real")
        print("cosh(x)       x es Real")
        print("arctanh(x)    |x| < 1")
        print("arccoth(x)    |x| > 1")
        print("pow(x, n)     x es Real, n es Real")
        print("sqrt(x, n=2)  x ≥ 0, n ≠ 0")
        print("abs(x)        x es Real")
        
        print("\nVariables disponibles:")
        print("(π, pi)       Numero pi")
        print("(τ, tau)      Numero tau (2π)")
        print("(e, euler)    Numero de euler")
        
        # Mostrar los comandos
        print("\n" + "-"*50)
        print("Comandos disponibles:")
        print("/save         Guardar log de los datos")
        print("/range        Cambiar el valor de n")
        print("/chgrad       Cambiar calculos a grados/radianes")
        print("/exit         Salir del programa")
        
        # Mostrar los comandos y resolver las operacioned
        print("\n" + "-"*50)
        print(end = global_result)
        
        # Intentar ejecutar el comando
        try:
            global_result = ""
            command = operation()
            
            # Realizar una accion dependiendo el comando
            if command == 0:
                save_log() # /save
            elif command == 1:
                Math.usesRadians(not Math.inRadians) # /chgrad
            elif command == 2:
                print("Cerrando...")
                sleep(0.750) # Sleep maneja segundos
                break # /exit
            #end if
        except InvalidCommandException as e:
            global_result = f"Error: {str(e)}\n"
        #end try
    #end if
#end def

# Ejecutar solo si es la funcion principal
if __name__ == "__main__":
    run()
#end if