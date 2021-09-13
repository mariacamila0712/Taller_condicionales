# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:10:57 2021

@author: Maria Camila
"""

# En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.

computadoras = int(input('Digite el número de computadoras: '))
valor_parcial = computadoras * 11000
if(computadoras < 5):
    descuento = valor_parcial * 0.1
    total = valor_parcial - descuento
    print(f'El valor a pagar es de: ${total:,}.')
elif(computadoras >= 5 & computadoras < 10):
    descuento = valor_parcial * 0.2
    total = valor_parcial - descuento
    print(f'El valor a pagar es de: ${total:,}.')
else:
    descuento = valor_parcial * 0.4
    total = valor_parcial - descuento
    print(f'El valor a pagar es de: ${total:,}.')
