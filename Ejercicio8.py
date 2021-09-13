# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:02:48 2021

@author: Maria Camila
"""

# Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.00 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses

valor_compra = float(input('Digite el valor de la compra: $'))
if(valor_compra > 500000):
    inversion = valor_compra * 0.55
    prestamo = valor_compra * 0.30
    credito = valor_compra * 0.15
else:
    inversion = valor_compra * 0.70
    prestamo = 0
    credito = valor_compra * 0.30
intereses = credito * 0.20
print(f'La cantidad de la inversion será de: ${inversion:,}')
print(f'El valor del préstamo será de: ${prestamo:,}')
print(f'El valor del crédito será de: ${credito:,}')
print(f'El valor de los intereses a pagar por crédito es de ${intereses:,}')
