# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:42:41 2021

@author: Maria Camila
"""

# Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.

monto = float(input('Digite el monto de la fianza: $'))
if(monto < 50000):
    cuota = monto * 0.3
    print(f'El valor de la cuota será de ${cuota:,}.')
else:
    cuota = monto * 0.2
    print(f'El valor de la cuota será de ${cuota:,}.')
