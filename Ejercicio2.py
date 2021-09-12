# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:24:21 2021

@author: Maria Camila
"""

# En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

numero_azar = int(input('Digite el número que escogió: '))
total_compra = float(input('Digite el valor total de la compra: $ '))

if (numero_azar < 74):
    descuento = total_compra * 0.15
    print(f'El descuento que se le hará será de ${descuento:,}')
elif(numero_azar >= 74):
    descuento = total_compra * 0.20
    print(f'El descuento que se le hará será de ${descuento:,}')
