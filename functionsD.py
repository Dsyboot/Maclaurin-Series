# Importar la excepcion Natural y la clase Decimal
from functions import NaturalNumberException
from decimal import Decimal, getcontext
getcontext().prec = 17 # Precision decimal de fabrica

# Clase estatica matematica con precision decimal
class DecimalMath:
    # Variables matematicas
    e = Decimal(2.718281828459045)
    pi = Decimal(3.141592653589793)
    tau = Decimal(6.283185307179586)
    n = 17 # Variable default
    inRadians = True # Variable de Grados/Radianes
    precision = 17
    
    # Metodo para cambiar la intensidad
    @staticmethod
    def intensity(val: int):
        DecimalMath.n = abs(val)
    #end def
        
    # Metodo para establecer la precision decimal
    @staticmethod
    def decimal_presision(val: int):
        if val != 0:
            DecimalMath.precision = val
            getcontext().prec = DecimalMath.abs(val)
        else:
            DecimalMath.precision = 1
            getcontext().prec = 1
        #end if
    #end def
    
    # Metodo para cambiar el modo de los grados
    @staticmethod
    def usesRadians(val: bool):
        DecimalMath.inRadians = val
    #end def
    
    # Metodo para convertir radianes a grados
    @staticmethod
    def radToDeg(radians: Decimal) -> Decimal:
        return radians * (Decimal(180) / DecimalMath.pi)
    #end def
    
    # Metodo para convertir grados a radianes
    @staticmethod
    def degToRad(grados: Decimal) -> Decimal:
        return grados * (DecimalMath.pi / Decimal(180))
    #end def
    
    # Metodo abs (por si no esta definida)
    @staticmethod
    def abs(x: Decimal) -> Decimal:
        return x if x >= 0 else x * Decimal(-1)
    #end def
    
    # Metodo pow (por si no esta definida)
    @staticmethod
    def pow(x: Decimal, n: Decimal) -> Decimal:
        return Decimal(x) ** Decimal(n)
    #end def
    
    # Metodo sqrt (por si no esta definida)
    @staticmethod
    def sqrt(x: Decimal, n=2) -> Decimal:
        # Validar 0
        if n == 0:
            if x == 1:
                return 1
            elif x == 0:
                raise ZeroDivisionError("La raiz de 0 evaluada en 0 es una forma indeterminada!")
            elif x > 0:
                return Decimal(float("inf"))
            elif x < 0:
                raise ZeroDivisionError(f"La raiz de {x} evaluada en 0 es una forma indeterminada!")
            #end if
        else:
            return DecimalMath.pow(x, 1 / n)
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
    def sin(x: Decimal) -> Decimal:
        # Convertir el input a radianes
        if not DecimalMath.inRadians:
            x = DecimalMath.degToRad(x)
        #end if
        
        result = Decimal(0.0)
        
        if DecimalMath.n >= 0:
            for i in range(DecimalMath.n+1):
                result += DecimalMath.pow(-1, i) * (DecimalMath.pow(x, 2 * i + 1) / DecimalMath.factorial(2 * i + 1))
            #end for
        #end if
        
        return result
    #end def
    
    # Metodo coseno usando serie de Maclaurin
    @staticmethod
    def cos(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        if not DecimalMath.inRadians:
            x = DecimalMath.degToRad(x)
        #end if
        
        if DecimalMath.n >= 0:
            for i in range(DecimalMath.n+1):
                result += DecimalMath.pow(-1, i) * (DecimalMath.pow(x, 2 * i) / DecimalMath.factorial(2 * i))
            #end for
        #end if
        
        return result
    #end def
    
    # Metodo seno inverso (arcoseno) usando serie de Maclaurin
    @staticmethod
    def arcsin(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        # Ejecutar si el dominio es -1 ≤ x ≤ 1
        if -1 <= x <= 1:
            if DecimalMath.n >= 0:
                for i in range(DecimalMath.n+1):
                    result += DecimalMath.factorial(2 * i) * (DecimalMath.pow(x, 2 * i + 1) / (DecimalMath.pow(4, i) * DecimalMath.pow(DecimalMath.factorial(i), 2) * (2 * i + 1)))
                #end for
            #end if
        else:
            raise ValueError("El dominio debe de ser -1 ≤ x ≤ 1")
        #end if
        
        if not DecimalMath.inRadians:
            result = DecimalMath.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo coseno inverso (arco-coseno) usando serie de Maclaurin
    @staticmethod
    def arccos(x: Decimal) -> Decimal:
        value = DecimalMath.arcsin(x)
        
        if not DecimalMath.inRadians:
            value = DecimalMath.degToRad(value)
            value = DecimalMath.radToDeg((DecimalMath.pi / 2) - value)
        else:
            value = (DecimalMath.pi / 2) - value
        #end if
        
        return value
    #end def
    
    # Metodo tangente inverso (arco-tangente) usando serie de Maclaurin
    @staticmethod
    def arctan(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        if DecimalMath.n >= 0:
            for i in range(DecimalMath.n+1):
                result += DecimalMath.pow(-1, i) * (DecimalMath.pow(x, 2 * i + 1) / (2 * i + 1))
        
        if not DecimalMath.inRadians:
            result = DecimalMath.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo exponencial usando serie de Maclaurin
    @staticmethod
    def exp(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        if DecimalMath.n >= 0:
            for i in range(DecimalMath.n+1):
                result += DecimalMath.pow(x, i) / DecimalMath.factorial(i)
        #end if
        
        return result
    #end def
    
    # Metodo logaritmo natural + 1 usando serie de Maclaurin
    @staticmethod
    def ln(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        if x > -1:
            if DecimalMath.n >= 0:
                for i in range(DecimalMath.n+1):
                    result += DecimalMath.pow(-1, i) * (DecimalMath.pow(x, i + 1) / (i + 1))
            #end if
        else:
            raise ValueError("El dominio debe de ser x > -1")
        #end if
        
        return result
    #end def
    
    # Metodo seno hiperbolico usando serie de Maclaurin
    @staticmethod
    def sinh(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        if DecimalMath.n >= 0:
            for i in range(DecimalMath.n+1):
                result += DecimalMath.pow(x, 2 * i + 1) / DecimalMath.factorial(2 * i + 1)
        #end if
        
        if not DecimalMath.inRadians:
            result = DecimalMath.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo coseno hiperbolico usando serie de Maclaurin
    @staticmethod
    def cosh(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        
        if DecimalMath.n >= 0:
            for i in range(DecimalMath.n+1):
                result += DecimalMath.pow(x, 2 * i) / DecimalMath.factorial(2 * i)
        #end if
        
        if not DecimalMath.inRadians:
            result = DecimalMath.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo arco tangente hiperbolica usando serie de Maclaurin
    @staticmethod
    def arctanh(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        x = abs(x) # |x| < 1
        
        if x < 1:
            if DecimalMath.n >= 0:
                for i in range(DecimalMath.n+1):
                    result += DecimalMath.pow(x, 2 * i + 1) / (2 * i + 1)
            #end if
        else:
            raise ValueError("El dominio debe de ser -1 < x < 1")
        #end if
        
        if not DecimalMath.inRadians:
            result = DecimalMath.radToDeg(result)
        #end if
        
        return result
    #end def
    
    # Metodo arco cotangente hiperbolica usando serie de Maclaurin
    @staticmethod
    def arccoth(x: Decimal) -> Decimal:
        result = Decimal(0.0)
        x = abs(x) # |x| > 1
        
        if x > 1:
            if DecimalMath.n >= 0:
                for i in range(DecimalMath.n+1):
                    result += 1 / (DecimalMath.pow(x, 2 * i + 1) * (2 * i + 1))
                #end for
            #end if
        else:
            raise ValueError("El dominio debe de ser |x| > 1")
        #end if
        
        if not DecimalMath.inRadians:
            result = DecimalMath.radToDeg(result)
        #end if
        
        return result
    #end def
#end class
    
# Clase para poder controlar de mejor manera la matematica con precision decimal
class DecimalSolver:
    # Diccionario para mapear nombres de Metodos a las funciones reales
    functions = {
        # Variables de Math
        "e": DecimalMath.e,
        "euler": DecimalMath.e,
        "pi": DecimalMath.pi,
        "tau": DecimalMath.tau,
        
        # Metodos de Math
        "abs": DecimalMath.abs,
        "pow": DecimalMath.pow,
        "sqrt": DecimalMath.sqrt,
        "fact": DecimalMath.factorial,
        "sin": DecimalMath.sin,
        "cos": DecimalMath.cos,
        "arcsin": DecimalMath.arcsin,
        "arccos": DecimalMath.arccos,
        "arctan": DecimalMath.arctan,
        "exp": DecimalMath.exp,
        "ln": DecimalMath.ln,
        "sinh": DecimalMath.sinh,
        "cosh": DecimalMath.cosh,
        "arctanh": DecimalMath.arctanh,
        "arccoth": DecimalMath.arccoth,
        
        # Opciones secretas :0
        "inf": Decimal(float("inf")),
        "radians": DecimalMath.degToRad,
        "degrees": DecimalMath.radToDeg
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