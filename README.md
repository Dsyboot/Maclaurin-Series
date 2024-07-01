# Maclaurin Series #
Este proyecto utiliza las series de maclaurin para poder evaluar las funciones trigonometricas, exponenciales y logaritmicas.

Las funciones estan creadas sin usar la libreria de math, asi que todos los calculos han sido programados y la precision dependera del valor que el usuario desee ingresar.

## Sintaxis y reglas
Las funciones definidas en este programa tienen reglas que siguen internamente, tales como valores permitidos, como ilegales

Algunos de esas funciones y sus reglas son:
```
fact(x)         x es Natural que incluye 0
sin(x)          x es Real
cos(x)          x es Real
arcsin(x)       -1 ≤ x ≤ 1       (x es real)
arccos(x)       -1 ≤ x ≤ 1       (x es real)
arctan(x)       x es Real
exp(x)          x es Real
ln(1 + x)       x > -1            (x es real)
sinh(x)         x es Real
cosh(x)         x es Real
arctanh(x)      |x| < 1          (x es real)
arccoth(x)      |x| > 1          (x es real)
pow(x, n)       x, n son Reales
sqrt(x, n=2)    x ≥ 0, n ≠ 0     (x, n son reales)
abs(x)          x es Real
```

Tambien se encuentran las siguientes variables:
```
(π, pi)         Numero pi
(τ, tau)        Numero tau (2π)
(e, euler)      Numero de euler
```

Para poder utilizar cualquiera de estas funciones y variables se puede utilizar cualquiera de los 3 programas incluidos en la carpeta "dist", la diferencia es que uno de ellos tiene interfaz grafica, y ese es el archivo .apk, un ejemplo de sintaxis es esta:

```python
sin(tau) + cos(45) - arctan(0.5) * pi - 5 
```

Esto es perfectamente valido en los programas, lo cual no generara ninguna excepcion al usarlo, tambien, es posible que el infinito pueda aparecer en ciertos casos, pero de igual forma no se tendra problemas con el.

## Secretos del programa
Existen variables/funciones secretas que en todas las compilaciones se puede utilizar. Aqui estan todos los secretos disponibles.

### Funcion de conversion a radianes
En los programas no esta explicito, pero se puede utilizar la funcion "radians" para convertir un valor/angulo a radianes

```python
radians(360) # Devuelve 2*pi => tau
radians(180) # Devuelve pi

# Ejemplo en los programas
radians(360) - radians(180) # Equivalente a pi 
```

### Funcion de conversion a grados
En los programas implicitamente se puede encontrar la funcion "degrees" que al igual que la funcion "radians", se encarga de convertir un valor/angulo, pero, en este caso, convierte radianes a grados

```python
degrees(tau) # Devuelve 360
degrees(pi) # Devuelve 180

# Ejemplo en los programas
degrees(tau) + degrees(pi / 4) - 5 # Equivalente a 400
```

### Variable ANS
Esta variable permite obtener el ultimo resultado registrado

```python
10 + 45 - 25 # 30
ANS * 2 # 60
ANS * 2 # 120
ANS * 4 # 480
```

### Variable/Valor Inf
Simplemente es el infinito, este infinito puede salir como resultado de ciertas operaciones, pero tambien se puede ingresar por si se quiere experimentar con el

```python
sqrt(1.1, 0) # Devuelve inf
sqrt(-0.1, 0) # Devuelve -inf
inf * 8 # Es inf
inf * -1 # Es -inf
```