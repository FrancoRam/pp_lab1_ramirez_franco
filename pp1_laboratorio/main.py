from desarrollo_funciones import *

#dream_team_app(lista_jugadores)

def mostrar_mayor_cantidad_de_logros(lista:list):
    
    #print(cadena)
    for jugador in lista:

        if re.search(r'\d+', jugador['logros'][0]):
            cadena1 = re.findall(r'\d+', jugador['logros'][0])
        print(cadena1)
mostrar_mayor_cantidad_de_logros(lista_jugadores)