# Juegos de azar, utilizando numeros aleatoreos.
import random

#Los datos al azar
def dados_JIR():
    dato1 = random.randint(1,6)
    dato2 = random.randint(1,6)
    print("Primer dato: ", dato1)
    print("Segundo dato: ", dato2)
    suma= dato1+dato2
    if suma==7:
        print("¡GANASTE!")
    else:
        print("Mejor suerte para la proxima")

def tombola():
    oportunidades = 10 
    for i in range(oportunidades):
        numeroSuerte = int(input('Escribe un numero del 1 al 10: '))
            # randint([inicio],[final])
        tombola = random.randint(1,10)
        print('El numero es ', tombola)
        if numeroSuerte==tombola:
            print('!Ganaste!')
            break
        else:
            print('Sigue paticipando')

# Menu de juego
def menu():
    i = 0
    while True:
        print("\nSeleciona el juego:")
        print("1. Tombola")
        print("2. Dados")
        print("3. Salir")
        i = int(input("Ingresa seleccion: "))
        if i == 1:
            print("\nTombola")
            tombola()
        elif i == 2:
            print("\nDados")
 adriancarreto
            dados_adriancarreto()

            dados_JIR()
main
        elif i == 3:
            break
        else:
            print("Opcion invalida")
adriancarreto
            
#Los datos al azar
def dados_adriancarreto():
    dato1 = random.randint(1,6)
Modifiquen la función por su usuario, donde se declara y cuando se llama.

def dados_adriancarreto():
Dentro de menu()

elif i == 2:
            print("\nDados")
            dados_adriancarreto()

if __name__ == "__main__":
    menu()
 main
