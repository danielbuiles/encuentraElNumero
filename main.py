#librerias nesesarias
from ascii import logo
import random

#Titulo o logo del juego importado desde el archivo ascii.py
print(logo)

#inputs ingresados por el usuario para configuracion basica del juego
vidas = int(input("\n Digite cuantas vidas desea tener: "))
maxNum = int(input("\n numero maximo al que debes adivinar: "))

#funcion principal del juego
def game(vidas,maxNum):
  randomNum = random.randint(0,maxNum)
  count = vidas-1
  for n in range(vidas):
    inpPuzzle = int(input(f"\nelija un numero del 0-{maxNum}: "))

    if inpPuzzle<randomNum:
      print(f"\nel numero escondido es mayor! te quedan {count-n} intentos\n")
    
    if inpPuzzle>randomNum:
      print(f"\nel numero escondido es menor! te quedan {count-n} intentos\n")

    if inpPuzzle==randomNum:
      print("\n🤩 Fantastico has encontrado el Numero escondido! 🤩\n")
      return
    

#ejecucion principal del juego
game(vidas,maxNum)