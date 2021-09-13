# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:43:07 2021

@author: Maria Camila
"""

# Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no
# comprar el automóvil.

valor_auto_terreno = float(input('Digite el valor del auto o terreno: $'))
valor_final_auto = float(input('Digite el valor final del auto: $'))
valor_final_terreno = float(input('Digite el valor final del terreno: $'))
incremento = valor_final_terreno - valor_auto_terreno
devaluacion = valor_auto_terreno - valor_final_auto
if(devaluacion <= incremento / 2):
    print('Usted si debe comprar el carro.')
else:
    print('Usted no debe comprar el carro.')
