# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:23:10 2021

@author: Maria Camila
"""

# Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume.

primer_numero = float(input('Digite el primer número: '))
segundo_numero = float(input('Digite el segundo número: '))

if(primer_numero == segundo_numero):
    resultado = primer_numero * segundo_numero
elif(primer_numero > segundo_numero):
    resultado = primer_numero - segundo_numero
else:
    resultado = primer_numero + segundo_numero
print(f'El resultdo es: {resultado}')
