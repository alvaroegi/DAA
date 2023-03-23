# This is a sample Python script.
import sys
import win32crypt

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

