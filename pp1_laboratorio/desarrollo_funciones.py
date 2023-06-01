import json
import re
import string



def parse_json(nombre_dic)->list:

    lista = []
    with open(nombre_dic, "r", encoding="utf-8") as archivo:
        diccionario = json.load(archivo)
        lista = diccionario["jugadores"]

    return lista

lista_jugadores = parse_json("dt.json")

#1
def mostrar_jugador_y_posicion(lista:list):
    '''
        Muestra los nombres de los que conforman al Dream Team  y sus posiciones
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.
        
    '''
    if(bool(lista)):
        for jugador in lista_jugadores:
            print("-------------------------------------------")
            print(jugador['nombre'],"\t\t|\t",jugador['posicion'])
            print("-------------------------------------------")
    else:
        print("error 01 - La lista es vacía")


def menu_indices(lista:list):
    '''
        Muestra en pantalla los nombres de los jugadores junto a su índice
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.  
    '''
    for indice in range(len(lista)):
        print(indice, ") ", lista[indice]['nombre'])
#-------------------
def estadisticas_jugador(lista:list, numero_indice:int):
    '''
        genera un diccionario de las estadísiticas de un jugador, en base a su índice
        (obs: si no encuentra el índice imprime en pantalla un error)
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.  
            numero_indice(int): número entero que indica el índice de uno de los jugadores
        return:
            retorna un diccionario
    ''' 
    diccionario_estadisticas = {}
    bandera = 0
    for indice in range(len(lista)):
        if indice == numero_indice: 
            diccionario_estadisticas[lista[indice]['nombre']] = lista[indice]['estadisticas']     
            bandera = 1
            break
    if bandera == 0:
        print("ERROR - NO SE ENCONTRÓ EL ÍNDICE BUSCADO - estadisticas_jugador() ")
    return diccionario_estadisticas

def imprimir_estadisticas(diccionario:dict, nombre_jugador:str):
    '''
        Imprime en pantalla de manera encolumnada las estadísiticas del jugador nombre_jugador
        
        Args:
            diccionario (dict): un diccionario que contiene las estadisiticas de nombre_jugador
            nombre_jugador(str): nombre de un jugador
    '''
    for key,valor in diccionario[nombre_jugador].items():
        print(key.replace("_"," "),":",valor )
#---------------
#2
def mostrar_estadisticas_jugadores(lista:list)->int:
    '''
        Permite seleccionar un jugador y mostrar sus estadísticas de juego.
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.  
        return:
            retorna el ÍNDICE del jugador seleccionado con sus estadísiticas.
    '''
    estadisticas = {}
    if(bool(lista)):
        while(True):
            menu_indices(lista)
            ind = input("Ingrese el nº del jugador que desea mostrar sus estadísticas: ")
            ind = int(ind)
            cantidad_jugadores = len(lista)
            if (int(ind) <= cantidad_jugadores and re.match(('[0-9]+'), str(ind))):
                nombre_jugador = lista[ind]['nombre']
                print(nombre_jugador, ":")
                estadisticas = estadisticas_jugador(lista, ind) #valor que retornará - diccionario
                imprimir_estadisticas(estadisticas, nombre_jugador)
                break
            else:
                print("\nERROR - algo salió mal")
            
    else:
        print("error 02 - la lista es vacía")
        ind = -1
    return ind



def generar_csv(nombre_archivo:str, lista:list, indice: int):
    with open(nombre_archivo, "w") as file:
        cabecera = "nombre,posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,promedio_asistencias_por_partido,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n"
        formato_mensaje = cabecera + (
            "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format(
                lista[indice]["nombre"],
                lista[indice]["posicion"],
                lista[indice]["estadisticas"]["temporadas"],
                lista[indice]["estadisticas"]["puntos_totales"],
                lista[indice]["estadisticas"]["promedio_puntos_por_partido"],
                lista[indice]["estadisticas"]["rebotes_totales"],
                lista[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                lista[indice]["estadisticas"]["asistencias_totales"],
                lista[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                lista[indice]["estadisticas"]["robos_totales"],
                lista[indice]["estadisticas"]["bloqueos_totales"],
                lista[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                lista[indice]["estadisticas"]["porcentaje_tiros_libres"],
                lista[indice]["estadisticas"]["porcentaje_tiros_triples"],
            )
        )
        file.write(formato_mensaje)


def preguntar_a_usuario_generar_csv(lista:list, ind:int):
    nombre_jugador = lista[ind]['nombre']
    opcion = input("\nDesea generar con las estadísticas del jugador {0} un archivo en formato CSV? (SI/NO)".format(nombre_jugador))
    if(opcion.upper() == 'SI'):
        generar_csv("estadistica_jugador.csv",lista, ind)
        print("\n*** generación de archivo CSV exitosa ***")
    else:
        print("\n*** generación de archivo CSV cancelada ***")
#4
def buscar_y_mostrar_por_jugador(lista:list):
    '''
        Busca y Muestra en caso de que haya coincidencia parcial los nombres de los que conforman 
        al Dream Team  y sus logros
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.
        return:
            retorna un booleano; True en caso de que haya elementos en la lista, False de lo contrario
    '''
    if(bool(lista)):
        ret = True
        mostrar_jugador_y_posicion(lista)
        nombre = input("Ingrese el nombre y apellido del jugador que desea visualizar sus logros en la NBA: ")
        if validar_nombre(nombre):
            lista_auxiliar = []
            for jugador in lista:
                if(re.search(nombre, jugador['nombre'], re.I)):
                    lista_auxiliar.append(jugador)
            mostrar_jugador_y_logros(lista_auxiliar)
    else:
        print("ERROR - la lista es vacía - mostrar_jugadores_y_posicion()")
        ret = False
    return ret
def mostrar_jugador_y_logros(lista):
    '''
        Muestra los nombres de los que conforman al Dream Team  y sus logros
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.
        return:
            retorna un booleano; True en caso de que haya elementos en la lista, False de lo contrario
    '''
    if(bool(lista)):
        ret = True
        print("** LOGROS ALCANZADOS EN LA NBA: ***\n")
        for jugador in lista:
            print(jugador['nombre']," :\n ","\n".join(jugador['logros']).strip())
            print("\n")
    else:
        print(" La lista es vacía")
        ret = False
    return ret
#--------------
def validar_nombre(nombre)->bool:
    '''
        Valida una cadena de caracteres
        
        Args:
            nombre (str): una cadena de caracteres, que puede ser el nombre de un jugador.
        return:
            retorna un booleano; True en caso de que haya coincidencias, False de lo contrario
    '''
    validacion = False
    if re.search('[a-zA-Z]', nombre) and nombre.isalpha:

        validacion = True
    else:
        print("error - ese nombre no coincide con ningún jugador de Dream Team")
    return validacion

#--------------

def dividir(dividendo:float, divisor:float)->float:
    '''
        permite dividir dos números y devolver el resultado
        
        Args:
            dividendo (float): un numero de tipo flotante
            divisor (float): un numero de tipo flotante
        return:
            retorna el resultado de la división.
    '''
    resultado = None
    if(divisor != 0):
        resultado = dividendo / divisor
    else:
        resultado = 0
    return resultado
# -------------------------------------

def calcular_promedio(lista:list, key)->float:
    '''
        calcula el promedio de 'key'
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.  
            key (str): clave perteneciente a un diccionario
        return:
            retorna el resultado de la división.
    '''
    promedio = -1
    if(bool(lista)):
        acumulador = 0
        contador = 0
        for jugador in lista:
            #obs: si los valores de los promedios(float) no estuvieran normalizados habría que hacerlo.
            if(bool(jugador) and type(jugador) == dict and (type(jugador['estadisticas'][key]) == int or type(jugador['estadisticas'][key]) == float)):
                acumulador = acumulador + jugador['estadisticas'][key]
                contador = contador + 1
        promedio = dividir(acumulador, contador)
    else:
        print("error - lista_aux vacía - calcular_promedio()")

    return promedio

def mostrar_promedio_puntos_por_partido(lista:list,key:str):
    if(bool(lista)):
        promedio=calcular_promedio(lista,key)
        print("El promedio de puntos por partido de TODO el equipo es de: {0:.2f} puntos\n".format(promedio))
    else:
        print("ERROR - la lista es vacía - mostrar_promedio_por_puntos_partido()")

# -------------------------------------

def quick_sort(lista: list, key: str, orden: str) -> list:
    """
    Ordena la 'lista' de manera 'orden' ("asc"/"desc") teniendo en cuenta la 'key'

    Args:
        lista : (list)
        key: (str): 
        orden: (str)

    return:
        lista_izq: (list)
    """
    if len(lista) <= 1:
        return lista
    lista_izq = []
    lista_der = []
    pivot = lista[0]

    for player in lista[1:]:
        if orden == "asc":
            if player[key] > pivot[key]:
                lista_der.append(player)
            else:
                lista_izq.append(player)
        elif orden == "desc":
            if player[key] > pivot[key]:
                lista_der.append(player)
            else:
                lista_izq.append(player)
    lista_izq = quick_sort(lista_izq, key, orden)
    lista_izq.append(pivot)
    lista_der = quick_sort(lista_der, key, orden)
    lista_izq.extend(lista_der)

    return lista_izq

def quick_sort_extendida(lista: list, key: str,key2:str, orden: str) -> list:
    """
    Ordena la 'lista' de manera 'orden' ("asc"/"desc") teniendo en cuenta la 'key'

    Args:
        lista : (list)
        key: (str): 
        orden: (str)

    return:
        lista_izq: (list)
    """
    if len(lista) <= 1:
        return lista
    lista_izq = []
    lista_der = []
    pivot = lista[0]

    for player in lista[1:]:
        if orden == "asc":
            if player[key2][key] > pivot[key2][key]:
                lista_der.append(player)
            else:
                lista_izq.append(player)
        elif orden == "desc":
            if player[key2][key] < pivot[key2][key]:
                lista_der.append(player)
            else:
                lista_izq.append(player)
    lista_izq = quick_sort_extendida(lista_izq, key, key2, orden)
    lista_izq.append(pivot)
    lista_der = quick_sort_extendida(lista_der, key, key2, orden)
    lista_izq.extend(lista_der)

    return lista_izq
#---------------------------------
def bubble_sort(lista: list, key: str, sentido: str):
    flag_swap = True
    rango = len(lista)
    while flag_swap:
        rango = rango - 1
        flag_swap = False
        for indice in range(rango):
            if sentido == "mayor":
                if (lista[indice]["estadisticas"][key] > lista[indice + 1]["estadisticas"][key]):
                    lista[indice], lista[indice + 1] = (lista[indice + 1],lista[indice],)
            else:
                if (lista[indice]["estadisticas"][key] < lista[indice + 1]["estadisticas"][key]):
                    lista[indice], lista[indice + 1] = (lista[indice + 1], lista[indice],)

def bubble_sort_lite(lista: list, key: str, sentido: str):
    for indice in range(len(lista) - 1):
        if sentido == "mayor":
            if (lista[indice]["estadisticas"][key] > lista[indice + 1]["estadisticas"][key]):
                lista[indice], lista[indice + 1] = (lista[indice + 1],lista[indice],)
        elif sentido == "desc":
            if (lista[indice]["estadisticas"][key] < lista[indice + 1]["estadisticas"][key]):
                lista[indice], lista[indice + 1] = (lista[indice + 1],lista[indice],)


def bubble_sort_asc(lista: list, key: str):
    for indice in range(len(lista) - 1):
        if len(lista[indice][key]) > len(lista[indice + 1][key]):
            lista[indice], lista[indice + 1] = (lista[indice + 1],lista[indice],)


#5
def mostrar_promedio_puntos_partido_y_ordenar(lista:list, key:str, orden:str):
    if(bool(lista)):
        mostrar_promedio_puntos_por_partido(lista,key)
        lista_aux = []
        lista_aux = lista[:]
        lista_aux_ordenada = quick_sort(lista_aux,'nombre',orden)
        for indice in range(len(lista_aux_ordenada)):
            print(lista_aux_ordenada[indice]['nombre'],":",lista_aux_ordenada[indice]['estadisticas'][key])

#-------------------------
#6
def ingresar_y_mostrar_jugador(lista:list):
    '''
        Permite ingreasar por usuario el nombre de un jugador y verifica si pertenece al salón de la fama
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.
        return:
            retorna un booleano; True en caso de que haya elementos en la lista, False de lo contrario
    '''
    ret = False
    if(bool(list)):
        logro = "Miembro del Salon de la Fama del Baloncesto"
        lista_aux = []
        while(True):
            nombre = input("Ingrese el nombre del jugador que desea conocer si pertenece al salón de la fama de la NBA: ")
            if validar_nombre(nombre):
                for jugador in lista:
                    if logro in jugador['logros'] and jugador['nombre'].casefold() == nombre.casefold():
                        lista_aux.append(jugador)

                if(bool(lista_aux)):
                    print("\n\tEste jugador ha alcanzado el salón de la fama, junto a otros logros:")
                    mostrar_jugador_y_logros(lista_aux)
                    ret = True
                else:
                    print("sin coincidencias")
                break
            else:
                print("ERROR - Ingrese un Nombre y Apellido correcto - no distingue entre MAY y MIN")
    return ret
#-------------
def calcular_max(lista:list, key):

    ret = -1
    if(bool(lista)):

        max_valor = lista[0]['estadisticas'][key]
        nombre_max_valor = lista[0]['nombre']
        for superheroe in lista:
            if(superheroe['estadisticas'][key] >= max_valor):
                max_valor = superheroe['estadisticas'][key]
                nombre_max_valor = superheroe['nombre']
        ret = ("\n\t** INFORME **:\nJugador con mayor {0}:\nNombre: {1} | {0}: {2}".format(quitar_guiones_bajo(key), nombre_max_valor, max_valor))
    return ret
#----------------------------------------
#

def calcular_min(lista:list, key):

    ret = -1
    if(bool(lista)):
        min_valor = lista[0]['estadisticas'][key]
        nombre_min_valor = lista[0]['nombre']
        for superheroe in lista:
            if(superheroe['estadisticas'][key] <= min_valor):
                min_valor = superheroe['estadisticas'][key]
                nombre_min_valor = superheroe['nombre']
        ret = ("\n\t** INFORME **:\nJugador con menor {0}:\nNombre: {1} | {0}: {2}".format(quitar_guiones_bajo(key), nombre_min_valor, min_valor))
    return ret
#-----------------------------------------
#7-10 | 12-13
def calcular_max_min_dato(lista:list, status:str, key:str)->str:
    ret=-1
    if(bool(lista)):
        if(status == 'maximo'):
            ret = calcular_max(lista, key)
        else:
            if(status == 'minimo'):
                ret = calcular_min(lista, key)
    return ret
#-----------------------------------------
def quitar_guiones_bajo(cadena)->str:
    if(len(cadena)>0):

        nueva_cadena = cadena.replace("_", " ")
        
    else:
        print("cadena vacía")
    return nueva_cadena
#10-11
def mostrar_promedios_mayores_a(lista:list, key:str):
    ret = False
    lista_aux = []
    if(bool(list)):
        while(True):
            valor = input("Ingrese el valor de referencia para mostrar los jugadores que lo superan: ")
            if es_numero_range(valor,1,40000):
                for jugador in lista:
                    if(jugador['estadisticas'][key] >= float(valor)):
                        lista_aux.append(jugador)
                if bool(lista_aux):
                   mostrar_nombre_y_caracteristica_jugador(lista_aux,key) 
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
    if(valor.isdigit()):
        valor = float(valor)
        if ((valor > min and valor < max)):
            ret = True
    return ret

def mostrar_nombre_y_caracteristica_jugador(lista:list, key:str):
    ret = False
    if(bool(lista)):
        ret = True
        for jugador in lista:
            print("\n-----------------------------------------")
            print("Nombre: {0}  -   Posicion: {1}\n{2}: {3}".format(
                                        jugador['nombre'],
                                        jugador['posicion'],
                                        quitar_guiones_bajo(key),
                                        jugador['estadisticas'][key]))
            print("-----------------------------------------")
    else:
        print("ERROR - la lista auxiliar es vacía")
    return ret
#20
def mostrar_promedios_mayores_a_sort(lista:list, key:str, key2:str):
    ret = False
    lista_aux = []
    if(bool(list)):
        while(True):
            valor = input("Ingrese el valor de referencia para mostrar los jugadores que lo superan: ")
            if es_numero_range(valor,1,40000):
                for jugador in lista:
                    if(jugador['estadisticas'][key] >= float(valor)):
                        lista_aux.append(jugador)
                if bool(lista_aux):
                   lista_aux = quick_sort(lista_aux, key2,'asc')
                   mostrar_nombre_y_caracteristica_jugador(lista_aux,key) 
                else:
                    print("sin coincidencias")
                break
            else:
                print("ERROR - Ingrese un VALOR correcto")

    else:
        print("ERROR - lista vacía ")

    return ret
#-----------------------------------------------------------------------
def calcular_promedio_prueba(lista:list, key, bandera)->float:
    '''
        calcula el promedio de 'key'
        
        Args:
            lista (list): una lista de diccionarios que contienen características de jugadores del Dream Team.  
            key (str): clave perteneciente a un diccionario
        return:
            retorna el resultado de la división.
    '''
    promedio = -1
    if(bool(lista) and bandera == True):
        acumulador = 0
        contador = 0
        for jugador in lista:
            #obs: si los valores de los promedios(float) no estuvieran normalizados habría que hacerlo.
            if(bool(jugador) and type(jugador) == dict and (type(jugador['estadisticas'][key]) == int or type(jugador['estadisticas'][key]) == float)):
                acumulador = acumulador + jugador['estadisticas'][key]
                contador = contador + 1
        promedio = dividir(acumulador, contador)
    else:
        if(bool(lista) and bandera == False):
            #lista =[]
            lista = quick_sort_extendida(lista, key, 'estadisticas', 'asc')

            acumulador = 0
            contador = 0
            for indice in range(len(lista)-1):
                if(bool(lista[indice]) and type(lista[indice]) == dict and (type(lista[indice]['estadisticas'][key]) == int or type(lista[indice]['estadisticas'][key]) == float)):
                    acumulador = acumulador + lista[indice]['estadisticas'][key]
                    contador = contador + 1
                    
                    
            promedio = dividir(acumulador, contador)
        else:
            print("error - lista_aux vacía - calcular_promedio()")

    return promedio
#------------------------------------------------------------
#16-18
def mostrar_promedio_jugadores_menos_uno(lista:list, key:str, bandera:bool):
    promedio = calcular_promedio_prueba(lista, key, bandera)
    print("------------------------")
    print("\t*** INFORME ***")
    print("{0} de los jugadores: {1:.2f}".format(quitar_guiones_bajo(key), promedio))
    print("------------------------")

# 23 BONUS ---------------------------------------------------------------------------
def exportar_tabla_posiciones_csv(lista: list, nombre_archivo):
    with open(nombre_archivo, "a") as archivo:
        formato_csv = "{0},{1},{2},{3},{4}\n".format(
            lista[0],
            lista[1],
            lista[2],
            lista[3],
            lista[4],)
        archivo.write(formato_csv)


def calcular_posicion(lista: list, key: str, indice_jugador: int):
    posicion_jugador = 0
    lista_aux = quick_sort_extendida(lista, key,'estadisticas', "asc")
    for indice in range(len(lista_aux)):
        if (lista_aux[indice]["estadisticas"][key]
            == lista[indice_jugador]["estadisticas"][key]):
            posicion_jugador = indice + 1

    return posicion_jugador


def bonus_jugadores(lista):
    lista_encabezado = ["nombre", "puntos", "rebotes", "asistencias", "robos"]
    exportar_tabla_posiciones_csv(lista_encabezado, "posiciones_jugadores.csv")
    
    for indice in range(len(lista)):
        lista_jugador_posiciones = []
        lista_jugador_posiciones.append(lista[indice]["nombre"])
        lista_jugador_posiciones.append(calcular_posicion(lista, "puntos_totales", indice))    
        lista_jugador_posiciones.append(calcular_posicion(lista, "rebotes_totales", indice))
        lista_jugador_posiciones.append(calcular_posicion(lista, "asistencias_totales", indice))
        lista_jugador_posiciones.append(calcular_posicion(lista, "robos_totales", indice))
        exportar_tabla_posiciones_csv(lista_jugador_posiciones, "posiciones_jugadores.csv")



#----------------------------- MENU --------------------------------
def imprimir_menu():
    # Mostrar menú de opciones

    print("\n\n")
    print("------------------------------------------------")
    print("\tMENÚ DE OPCIONES:")
    print("1. Mostrar el nombre y posicion de cada jugador")
    print("2. Mostrar estadísticas de jugador a traves de su índice")
    print("3. Convertir a archivo CSV")
    print("4. Buscar por nombre un jugador y mostrar sus Logros en NBA")
    print("5. Calcular y mostrar el promedio de puntos por partido")
    print("6. Ingresar y mostrar si jugador pertenece Salón de la Fama del Baloncesto.")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo")
    print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales")
    print("10. Mostrar los jugadores que han promediado más puntos por partido por valor ingresado")
    print("11. Mostrar los jugadores que han promediado más rebotes por partido por valor ingresado")
    print("12. Mostrar los jugadores que han promediado más asistencias por partido por valor ingresado")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales")
    print("15. Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a valor ingresado")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18. mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a valor ingresado")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20. mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor")
    print("23. bonus")
    print("0. Salir del programa")
    print("------------------------------------------------")
    print("\n\n")

def validar_entero(cadena:str)->bool:
    valor = True
    bandera = 0
    for indice in range(len(cadena)):
        if(bandera == 0 and not cadena[indice].isdigit()):
            valor = False
            bandera = 1
    return valor

def menu_principal():
    ret = -1
    imprimir_menu()
    ingreso = input("Ingrese una de las opciones:  ")
    
    if validar_entero(ingreso) and ( int(ingreso) >= 0 and int(ingreso) <= 27):
        ingreso = int(ingreso)
        ret = ingreso
    return ret

def dream_team_app(lista:list):
    while(True):
        opcion = menu_principal()
        if opcion == 1:
            mostrar_jugador_y_posicion(lista)
        elif opcion == 2:
            indice_estadisticas_jugadores = mostrar_estadisticas_jugadores(lista)
        elif opcion == 3:
            preguntar_a_usuario_generar_csv(lista, indice_estadisticas_jugadores)
        elif opcion == 4:
            buscar_y_mostrar_por_jugador(lista)
        elif opcion == 5:
            mostrar_promedio_puntos_partido_y_ordenar(lista, 'promedio_puntos_por_partido', 'asc')
        elif opcion == 6:
            ingresar_y_mostrar_jugador(lista)
        elif opcion == 7:
            print(calcular_max_min_dato(lista,"maximo", 'rebotes_totales'))
        elif opcion == 8:
            print(calcular_max_min_dato(lista,"maximo", 'porcentaje_tiros_de_campo'))
        elif opcion == 9:
            print(calcular_max_min_dato(lista,"maximo", 'asistencias_totales'))
        elif opcion == 10:
            mostrar_promedios_mayores_a(lista, "promedio_puntos_por_partido")
        elif opcion == 11:
            mostrar_promedios_mayores_a(lista, "promedio_rebotes_por_partido")           
        elif opcion == 12:
            mostrar_promedios_mayores_a(lista, "promedio_asistencias_por_partido")           
        elif opcion == 13:
            print(calcular_max_min_dato(lista,"maximo", 'robos_totales'))
        elif opcion == 14:
            print(calcular_max_min_dato(lista,"maximo", 'bloqueos_totales'))
        elif opcion == 15:
            mostrar_promedios_mayores_a(lista, "porcentaje_tiros_libres")
        elif opcion == 16:
            mostrar_promedio_jugadores_menos_uno(lista, 'promedio_puntos_por_partido', bandera=False)
        elif opcion == 17:
            pass
        elif opcion == 18:
            mostrar_promedios_mayores_a_sort(lista, 'porcentaje_tiros_libres', 'nombre')
        elif opcion == 19:
            print(calcular_max_min_dato(lista, 'maximo', 'temporadas'))
            #en este caso se debería utilizar otra función o modificar la utilizada para el caso de que exista más de un máximo.
        elif opcion == 20:
            mostrar_promedios_mayores_a_sort(lista, 'porcentaje_tiros_de_campo', 'posicion')
        elif opcion == 23:
            bonus_jugadores(lista_jugadores)
        elif opcion == -1:
            pass
        elif opcion == 0:
            break
    

#  ---------- \\ Termina el desarrollo de las funciones \\ ----------------------