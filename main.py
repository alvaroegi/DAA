# This is a sample Python script.
import sys


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma(lista):
    n = len(lista)
    if(n == 0):
        return 0
    else:
        return lista[-1] + suma(lista[:n-1])

def suma2(lista):
    n = len(lista)
    if(n == 0):
        return 0
    else:
        return lista[0] + suma2(lista[1:n])

def suma3(lista):
    mitad = len(lista) // 2
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return suma3(lista[:mitad]) + suma3(lista[mitad:])

def suma4(lista, inf, sup):
    if inf>sup:
        return 0
    else:
        return lista[inf] + suma4(lista, inf+1, sup)

def suma5(lista, inf, sup):
    if inf > sup:
        return 0
    elif inf == sup:
        return lista[inf]
    else:
        mitad = (sup + inf) // 2
        return suma5(lista, inf, mitad) + suma5(lista, mitad+1, sup)

print(suma([1,2,3,4]))
print(suma2([1,2,3,4]))
print(suma3([1,2,3,4]))
print(suma4([1,2,3,4], 0, len([1,2,3,4])-1))
print(suma5([1,2,3,4], 0, len([1,2,3,4])-1))


def sumaDig(num):
    if (num%10 == 0):
        return 0
    else:
        return num%10 + sumaDig(num//10)

print(sumaDig(3652))

def sumaLenta(a,b):
    if (a == 0):
        return b
    else:
        return sumaLenta(a-1,b+1)

def sumaLenta2(a,b):
    if (a == 0):
        return b
    elif (b == 0):
        return a
    else:
        return sumaLenta2(a-1,b-1)+1+1

print(sumaLenta(2,10))
print(sumaLenta2(2,10))

def maxLista(lista):
    if (len(lista) == 1):
        return lista[0]
    else:
        return max(maxLista(lista[1:]), lista[0])


print(maxLista([4,3,5,1]))

def potencia(a, n): #a^n
    if (n == 1):
        return a
    else:
        return a*(potencia(a, n-1))

print(potencia(2,10))

def escribir(s):
    if (len(s) == 0):
        return print()
    else:
        print(s[0])
        escribir(s[1:])

escribir("Hola")

def sumatorio(m,n,g):
    if(m == n):
        return g(n)
    else:
        return g(m) + sumatorio(m+1,n,g)

def sumatorio2(m,n,g):
    if(n == m):
        return g(m)
    else:
        return sumatorio2(m,n-1,g) + g(n)

def sumatorio3(m,n,g):
    mitad = (n+m) // 2
    if (m == n):
        return g(m)
    else:
        return sumatorio3(m,mitad,g) + sumatorio3(mitad+1,n,g)
def g(x):
    return x**2

print(sumatorio(3,6,g))
print(sumatorio2(3,6,g))
print(sumatorio3(3,6,g))

def containsNumber(n,a):
    if(n == a):
        return True
    elif(n % 10 == a):
        return True
    elif (n // 10 == 0):
        return False
    else:
        return containsNumber(n // 10,a)

print(containsNumber(132237540982507329875435,9))

def cambioBase(n,b):
    if(n // b == 0):
        return n
    else:
        return  10*cambioBase(n // b,b) + (n%b)

print(cambioBase(142,5))

def polinomio(n,p):
    lon = len(p)
    if(lon == 1):
        return p[0]
    else:
        return p[lon-1]*(n)**(lon-1) + polinomio(n,p[:-1])

def polinomio2(n,p):
    lon = len(p)
    if(lon == 1):
        return p[0]
    else:
        return p[0] + n*polinomio2(n,p[1:])

print(polinomio(3,[2,-4,5]))
print(polinomio2(3,[2,-4,5]))

def busLineal(n,p):
    l = len(p)
    if(l == 0):
        return -1
    elif(p[0] == n):
        return 1
    else:
        return 1 + busLineal(n,p[1:])

print(busLineal(9,[3,4,5,2,1,2,2,2,9]))

def busOrdenada(n,p):
    l = len(p)
    if(l == 0) or (n < p[0]):
        return -1
    elif(p[0] == n):
        return 1
    else:
        return 1 + busOrdenada(n,p[1:])

print(busOrdenada(9,[3,4,5,2,1,2,2,2,9]))

def subirEsc(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    else:
        return subirEsc(n-1) + subirEsc(n-2)

print(subirEsc(5))

def Manhattan(x,y):
    if (x == 0) or (y == 0):
        return 1
    else:
        return Manhattan(x-1,y) + Manhattan(x,y-1)

print(Manhattan(3,3))

def biseccion(a,b,f,e):
    mitad = (a+b)/2
    if (f(mitad) == 0) or (b-a <= 2*e):
        return mitad
    elif (f(a)*f(b) < 0):
        return biseccion(a,mitad,f,e)
    else:
        return biseccion(mitad,b,f,e)

def f(x):
    return x-2

print(biseccion(1,2,f,0.001))

def insertSort(n,l,p):
    lon = len(l)
    if(lon == 0):
        return p
    elif(n > l[lon-1]):
        aux = [None]*len(p)
        for i in range(lon,len(p)-1):
            aux[i+1] = p[i]
        p = aux
        p[lon] = n
        while (lon != 0):
            p[lon-1] = l[lon-1]
            lon = lon-1
        return p
    else:
        p[lon-1] = l[lon-1]
        return insertSort(n,l[:-1],p)

print(insertSort(-2,[-3,0,3,8,11],[None]*6))

