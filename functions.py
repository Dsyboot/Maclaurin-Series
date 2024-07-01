# Excepcion de dato invalido
class InvalidTypeData(Exception):
    pass
#end class

# Excepcion de numeros naturales
class NaturalNumberException(Exception):
    pass
#end class

# Excepcion de comandos
class InvalidCommandException(Exception):
    pass
#end class

# Clase estatica matematica
class Math:
    # Variables matematicas
    e = 2.718281828459045
    pi = 3.141592653589793
    tau = 6.283185307179586
    n = 17 # Variable default
    inRadians = True # Variable de Grados/Radianes
    
    # Metodo para cambiar la intensidad
    @staticmethod
    def intensity(val: int):
        Math.n = abs(val)
    #end def
    
    # Metodo para cambiar el modo de los grados
    @staticmethod
    def usesRadians(val: bool):
        Math.inRadians = val
    #end def
    
    # Metodo para convertir radianes a grados
    @staticmethod
    def radToDeg(radians: float) -> float:
        return radians * (180 / Math.pi)
    #end def
    
    # Metodo para convertir grados a radianes
    @staticmethod
    def degToRad(grados: float) -> float:
        return grados * (Math.pi / 180)
    #end def
    
    # Metodo abs (por si no esta definida)
    @staticmethod
    def abs(x: float):
        return x if x >= 0 else x * -1
    #end def
    
    # Metodo pow (por si no esta definida)
    @staticmethod
    def pow(x, n):
        return x ** n
    #end def
    
    # Metodo sqrt (por si no esta definida)
    @staticmethod
    def sqrt(x: float, n=2):
        # Validar 0
        if n == 0:
            if x == 1:
                return 1
            elif x == 0:
                raise ZeroDivisionError("La raiz de 0 evaluada en 0 es una forma indeterminada!")
            elif x > 1:
                return float("inf")
            elif x < 1:
                return float("inf") * -1
            #end if
        else:
            return Math.pow(x, 1 / n)
        #end if
    #end def
    
    # Factorial sin recursividad
    @staticmethod
    def factorial(n: int) -> int:
        if n >= 0:
            result = 1
            
            try:
                for i in range(1, n + 1):
                    result *= i
                #end for
            except TypeError:
                raise NaturalNumberException("La factorial solo acepta numeros naturales!")
            except:
                raise OverflowError("La factorial es extremadamente grande!")
        else:
            raise SyntaxError("La factorial negativa no esta definida!")
        #end if
        
        return result
    #end def
    
    # Metodo seno usando serie de Maclaurin
    @staticmethod
    def sin(x: float) -> float:
        # Convertir el input a radianes
        if not Math.inRadians:
            x = Math.degToRad(x)
        #end if
        
        result = 0.0
        
        if Math.n >= 0:
            for i in range(Math.n+1):
                result += Math.pow(-1, i) * (Math.pow(x, 2 * i + 1) / Math.factorial(2 * i + 1))
            #end for
        #end if
        
        return result
    #end def
    
    # Metodo coseno usando serie de Maclaurin
    @staticmethod
    def cos(x: float) -> float:
        result = 0.0
        
        if not Math.inRadians:
            x = Math.degToRad(x)
        #end if
        
        if Math.n >= 0:
            for i in range(Math.n+1):
                result += Math.pow(-1, i) * (Math.pow(x, 2 * i) / Math.factorial(2 * i))
            #end for
        #end if
        
        return result
    #end def
    
    # Metodo seno inverso (arcoseno) usando serie de Maclaurin
    @staticmethod
    def arcsin(x: float) -> float:
        result = 0.0
        
        # Ejecutar si el dominio es -1 ≤ x ≤ 1
        if -1 <= x <= 1:
            if Math.n >= 0:
                for i in range(Math.n+1):
                    result += Math.factorial(2 * i) * (Math.pow(x, 2 * i + 1) / (Math.pow(4, i) * Math.pow(Math.factorial(i), 2) * (2 * i + 1)))
                #end for
            #end if
        else:
            raise ValueError("El dominio debe de ser -1 ≤ x ≤ 1")
        #end if
        
        if not Math.inRadians:
            result = Math.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo coseno inverso (arco-coseno) usando serie de Maclaurin
    @staticmethod
    def arccos(x: float) -> float:
        value = Math.arcsin(x)
        
        if not Math.inRadians:
            value = Math.degToRad(value)
            value = Math.radToDeg((Math.pi / 2) - value)
        else:
            value = (Math.pi / 2) - value
        #end if
        
        return value
    #end def
    
    # Metodo tangente inverso (arco-tangente) usando serie de Maclaurin
    @staticmethod
    def arctan(x: float) -> float:
        result = 0.0
        
        if Math.n >= 0:
            for i in range(Math.n+1):
                result += Math.pow(-1, i) * (Math.pow(x, 2 * i + 1) / (2 * i + 1))
        
        if not Math.inRadians:
            result = Math.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo exponencial usando serie de Maclaurin
    @staticmethod
    def exp(x: float) -> float:
        result = 0.0
        
        if Math.n >= 0:
            for i in range(Math.n+1):
                result += Math.pow(x, i) / Math.factorial(i)
        #end if
        
        return result
    #end def
    
    # Metodo logaritmo natural + 1 usando serie de Maclaurin
    @staticmethod
    def ln(x: float) -> float:
        result = 0.0
        
        if x > -1:
            if Math.n >= 0:
                for i in range(Math.n+1):
                    result += Math.pow(-1, i) * (Math.pow(x, i + 1) / (i + 1))
            #end if
        else:
            raise ValueError("El dominio debe de ser x > -1")
        #end if
        
        return result
    #end def
    
    # Metodo seno hiperbolico usando serie de Maclaurin
    @staticmethod
    def sinh(x: float) -> float:
        result = 0.0
        
        if Math.n >= 0:
            for i in range(Math.n+1):
                result += Math.pow(x, 2 * i + 1) / Math.factorial(2 * i + 1)
        #end if
        
        if not Math.inRadians:
            result = Math.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo coseno hiperbolico usando serie de Maclaurin
    @staticmethod
    def cosh(x: float) -> float:
        result = 0.0
        
        if Math.n >= 0:
            for i in range(Math.n+1):
                result += Math.pow(x, 2 * i) / Math.factorial(2 * i)
        #end if
        
        if not Math.inRadians:
            result = Math.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo arco tangente hiperbolica usando serie de Maclaurin
    @staticmethod
    def arctanh(x: float) -> float:
        result = 0.0
        x = abs(x) # |x| < 1
        
        if x < 1:
            if Math.n >= 0:
                for i in range(Math.n+1):
                    result += Math.pow(x, 2 * i + 1) / (2 * i + 1)
            #end if
        else:
            raise ValueError("El dominio debe de ser -1 < x < 1")
        #end if
        
        if not Math.inRadians:
            result = Math.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo arco cotangente hiperbolica usando serie de Maclaurin
    @staticmethod
    def arccoth(x: float) -> float:
        result = 0.0
        x = abs(x) # |x| > 1
        
        if x > 1:
            if Math.n >= 0:
                for i in range(Math.n+1):
                    result += 1 / (Math.pow(x, 2 * i + 1) * (2 * i + 1))
                #end for
            #end if
        else:
            raise ValueError("El dominio debe de ser |x| > 1")
        #end if
        
        if not Math.inRadians:
            result = Math.radToDeg(result)
        #end if
        
        return result
    #end def
#end class

# Clase para poder controlar de mejor manera la matematica
class Solver:
    # Diccionario para mapear nombres de Metodos a las funciones reales
    functions = {
        # Variables de Math
        "e": Math.e,
        "euler": Math.e,
        "pi": Math.pi,
        "tau": Math.tau,
        
        # Metodos de Math
        "abs": Math.abs,
        "pow": Math.pow,
        "sqrt": Math.sqrt,
        "fact": Math.factorial,
        "sin": Math.sin,
        "cos": Math.cos,
        "arcsin": Math.arcsin,
        "arccos": Math.arccos,
        "arctan": Math.arctan,
        "exp": Math.exp,
        "ln": Math.ln,
        "sinh": Math.sinh,
        "cosh": Math.cosh,
        "arctanh": Math.arctanh,
        "arccoth": Math.arccoth,
        
        # Opciones secretas :0
        "inf": float("inf"),
        "radians": Math.degToRad,
        "degrees": Math.radToDeg
    }
    
    # Metodo complejo para evaluar una expresion
    def evaluate_expression(self, expression) -> tuple:
        try:
            result = (eval(expression, {"__builtins__": None}, self.functions), False)
        except ZeroDivisionError:
            result = ("Forma Indeterminada", True)
        except SyntaxError:
            result = ("Error de calculo", True)
        except TypeError:
            result = ("Error de sintaxis", True)
        except NameError:
            result = ("Error de sintaxis", True)    
        except ValueError:
            result = ("Error en el dominio", True)
        except NaturalNumberException:
            result = ("Numero natural esperado", True)
        except OverflowError:
            result = ("Resultado muy grande", True)
        #end try
        
        return result # Funcion, Error
    #end def
    
    # Metodo simple para resolver una ecuacion
    def evaluate(self, expression):
        fun, _ = self.evaluate_expression(expression)
        
        return fun # Funcion
    #end def
#end class