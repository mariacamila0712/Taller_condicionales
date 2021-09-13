# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:30:10 2021

@author: Maria Camila
"""

# Leer tres números diferentes e imprimir el número mayor de los
# tres.
primer_numero = float(input('Digite el primer número: '))
segundo_numero = float(input('Digite el segundo número: '))
tercer_numero = float(input('Digite el primer número: '))
if((primer_numero > segundo_numero) & (primer_numero > tercer_numero)):
    print(f'El número mayor es el primer numero es decir el {primer_numero}')
elif((segundo_numero > primer_numero) & (segundo_numero > tercer_numero)):
    print(f'El número mayor es el segundo numero es decir el {segundo_numero}')
else:
    print(f'El número mayor es el tercer numero es decir el {tercer_numero}')
