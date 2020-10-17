# el dado va a tirarse solo y va a caer en un pais, el juego preguntara al jugador si quiere comprar o no
# el jugador decidira si comprar o no, y al finalizar el juego imprimira los paises que compro

from random import randint
nameP1 = input('Ingrese el nombre del jugador: ')
print ("""
                COMIENZA EL JUEGO
""")
limite = 8
posicion = 0
continueGame = True
paises = ['Comienzo','Granada', 'Sevilla', 'Madrid', 'Isla Bali', 'Hong Kong', 'Beijing', 'Shangai', 'Isla Perdida', 'Venecia', 
'Milan', 'Roma', 'Ruleta', 'hamburgo', 'Isla Chipre', 'Berlin', 'Copa Mundial', 'Londres', 'Isla Dubai', 'Sidney', 'Ruleta 2', 
'Chicago', 'Las Vegas', 'New York', 'Aeropuerto', 'Isla Nice', 'Lyon', 'Paris', ' Ruleta 3', 'Osaka', 'AFIP', 'Tokyo', 'FIN' ]

def lanzar_dado():
    return randint(1, 6)

# tirar dado, sumar una vuelta y sumar el N a dado
while posicion < limite:
    dado1 = lanzar_dado()
    print(f'Numero {dado1}')
    print(paises[dado1])
    posicion += 1
    nueva_posicion = posicion + dado1
    print (nueva_posicion)
    print (f'Nuevo casillero {nueva_posicion}')
    posicion += 1
    nueva_posicion = posicion + dado1
    print (nueva_posicion)
    print (f'Nuevo casillero {nueva_posicion}')
    # if posicion <limite:
    #     # print (paises[dado1])
    #     posicion += dado1
    # else:
        # print(2)

