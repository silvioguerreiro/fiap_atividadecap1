import math
import csv
import os

# Item d.
culturas_data = {
    "soja": [],
    "milho": [],
}

produtos_disponiveis = {
    "1": "Fosfato",
    "2": "Ureia",
    "3": "Cloreto de Potássio",
    "4": "Calcário"
}

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_quadrado(lado):
    return lado * lado

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Item a. suporte a 2 tipos de culturas
def escolher_cultura():
    print("\nEscolha a cultura:")
    print("1. Soja")
    print("2. Milho")
    opcao = input("Selecione uma opção para cultura: ")

    if opcao == "1":
        return "soja"
    elif opcao == "2":
        return "milho"
    else:
        print("Opção inválida.")
        return None

# Item c. Cálculo do manejo de insumos
def escolher_produto():
    print("\nEscolha o produto:")

    # Item f. Usar rotinas de loop e decisão. (if/else/for)
    for codigo, nome in produtos_disponiveis.items():
        print(f"{codigo}. {nome}")
    opcao = input(f"\nSelecione uma opção para produto: ")

    if opcao in produtos_disponiveis:
        produto_escolhido = produtos_disponiveis[opcao]
        print(f"Produto selecionado: {produto_escolhido}")
        return produto_escolhido
    else:
        print("Opção inválida.")
        return None

