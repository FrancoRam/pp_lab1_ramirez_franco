from desarrollo_funciones import *

#dream_team_app(lista_jugadores)

'''
10
Permitir al usuario ingresar un valor 
y mostrar los jugadores que han promediado más puntos por partido que ese valor
'''
def mostrar_promedios_mayores_a(lista:list, key:str):
    ret = False
    lista_aux = []
    if(bool(list)):
        while(True):
            valor = input("Ingrese el valor de referencia para mostrar los jugadores que lo superan")
            if es_numero_range(valor,1,40):
                for jugador in lista:
                        if(jugador['estadisticas'][key] >= valor):
                            lista_aux.append("jugador")
                else:
                    print("sin coincidencias")
                break
            else:
                print("ERROR - Ingrese un VALOR correcto")

    else:
        print("ERROR - lista vacía ")

    return ret

def es_numero_range(valor, min, max):
    ret = False
    valor = float(valor)
    if valor > min and valor < max and valor.isdigit():
        ret = True
    return ret