# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:21:47 2021

@author: Maria Camila
"""

# Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.

valor = float(input('Digite el valor del aparato a comprar: $'))
marca = str(input('Digite la marca del aparato a comprar: '))
valor_final = 0
iva = valor * 0.16
if(valor >= 2000):
    valor_final = valor - (valor * 0.1) + iva
else:
    valor_final = valor + iva
if(marca == "nosy"):
    valor_final = valor_final - (valor * 0.05)
else:
    valor_final = valor_final
print(f'El valor final es de : ${valor_final:,}')
