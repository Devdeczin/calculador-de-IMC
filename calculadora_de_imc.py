import time
import sys
import os
from rich import print as rprint

def delay_print(text, color="white"):
    for char in text:
        rprint(f"[{color}]{char}[/{color}]", end='')
        sys.stdout.flush()
        time.sleep(0.05)
    rprint()

def delay_input(prompt, color="white"):
    for char in prompt:
        rprint(f"[{color}]{char}[/{color}]", end='')
        sys.stdout.flush()
        time.sleep(0.05)
    return input()

def progress_bar():
    for i in range(21):
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        time.sleep(0.1)

def clear():
    os.system('clear')

def IMC(peso, altura):
    return peso / (altura ** 2)

def calcular_imc(peso, altura):
    progress_bar()
    clear()
    if peso <= 0 or altura <= 0:
        delay_print("Peso e altura devem ser valores positivos. Tente novamente.", color="red")
        return

    imc = IMC(peso, altura)

    delay_print(f"Seu IMC é: {imc:.2f}", color="green")

    peso_min = 18.5 * (altura ** 2)
    peso_max = 24.9 * (altura ** 2)

    if imc < 18.5:
        delay_print("Você está abaixo do peso normal.", color="yellow")
        delay_print(f"Para sua altura, o peso ideal seria entre {peso_min:.2f} kg e {peso_max:.2f} kg.", color="yellow")
    elif imc >= 18.5 and imc < 24.9:
        delay_print("Você está dentro da faixa de peso normal.", color="green")
    elif imc >= 24.9 and imc < 29.9:
        delay_print("Você está com sobrepeso.", color="yellow")
        delay_print(f"Para sua altura, o peso ideal seria entre {peso_min:.2f} kg e {peso_max:.2f} kg.", color="yellow")
    elif imc >= 29.9:
        delay_print("Você está obeso.", color="red")
        delay_print(f"Para sua altura, o peso ideal seria entre {peso_min:.2f} kg e {peso_max:.2f} kg.", color="yellow")

def calculadora_de_imc():
    delay_print("Bem-vindo à calculadora de IMC (Índice de Massa Corporal)")
    delay_print("AVISO: Os cálculos são feitos com base na altura em metros e peso em quilogramas, a situação pode variar para cada pessoa", color="red")
    try:
        peso = float(delay_input("Coloque seu peso em kg: "))
        altura = float(delay_input("Coloque sua altura em metros: "))
    except ValueError:
        delay_print("Por favor, insira valores válidos.", color="red")
        return
    calcular_imc(peso, altura)

if __name__ == "__main__":
    calculadora_de_imc()
