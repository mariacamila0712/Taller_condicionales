# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:14:07 2021

@author: Maria Camila
"""

# Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.

camisas = int(input('Digite el número de camisas a comprar: '))
valor_uni = float(input('Digite el valor unitario de las camisas: $'))
valor_total = camisas * valor_uni

if(camisas >= 3):
    descuento = valor_total * 0.3
    valor_final = valor_total - descuento
    print(f'El valor a pagar es de: ${valor_final:,} y se le aplicó un 30% descuento.')
else:
    descuento = valor_total * 0.1
    valor_final = valor_total - descuento
    print(f'El valor a pagar es de: ${valor_final:,} y se le aplicó un 10% descuento.')
