# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:52:36 2021

@author: Maria Camila
"""

# Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.

puntos = float(input('Digite el promedio de puntos: '))
ganancias = float(input('Digite el valor de las ganancias diarias: $'))
if(puntos > 170):
    multa = ganancias * 0.5
    perdida = ganancias + multa
    print(f'El valor de la multa sera de: ${perdida:,}.')
else:
    print('Usted no tendrá multa.')
