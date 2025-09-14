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

# Item b. Cálculo de área de plantio para cada cultura
def escolher_figura_geometrica():
    print("\nEscolha a figura geométrica para o cálculo da área:")
    print("1. Retângulo")
    print("2. Quadrado")
    print("3. Círculo")
    print("4. Triângulo")
    opcao_figura = input("\nSelecione uma opção para figura geométrica: ")

    if opcao_figura == "1":
        return "retangulo"
    elif opcao_figura == "2":
        return "quadrado"
    elif opcao_figura == "3":
        return "circulo"
    elif opcao_figura == "4":
        return "triangulo"
    else:
        print("Opção de figura geométrica inválida.")
        return None

def entrada_dados():
    print("\n--- Entrada de Dados ---")
    cultura = escolher_cultura()
    if not cultura:
        return

    print(f"\nInserindo dados para {cultura.capitalize()}.")
    print(f"---------------------------------------------------")

    # Cálculo de área de plantio
    figura_geometrica = escolher_figura_geometrica()
    if not figura_geometrica:
        return

    area = 0
    try:
        if figura_geometrica == "retangulo":
            print("Cálculo de área para Retângulo.")
            print()
            base = float(input("Digite o comprimento da lavoura em metros: "))
            altura = float(input("Digite a largura da lavoura em metros: "))
            print()
            area = calcular_area_retangulo(base, altura)
        elif figura_geometrica == "quadrado":
            print("Cálculo de área para Quadrado.")
            lado = float(input("Digite o lado da lavoura em metros: "))
            print()
            area = calcular_area_quadrado(lado)
        elif figura_geometrica == "circulo":
            print("Cálculo de área para Círculo.")
            raio = float(input("Digite o raio da lavoura em metros: "))
            print()
            area = calcular_area_circulo(raio)
        elif figura_geometrica == "triangulo":
            print("Cálculo de área para Triângulo.")
            base = float(input("Digite a base da lavoura em metros: "))
            altura = float(input("Digite a altura da lavoura em metros: "))
            print()
            area = calcular_area_triangulo(base, altura)
        
        print(f"Área de plantio para {cultura.capitalize()}: {area:.2f} m²")
    except ValueError:
        print("\n Entrada inválida para dimensões. Por favor, digite números.")
        return

    print("\n--- Manejo de Insumos ---")
    produto = escolher_produto()
    if not produto:
        return

    try:
        quantidade_por_metro = float(input("Quantidade necessária por metro (mL/metro ou g/metro): "))
        num_ruas = int(input("Número de ruas na lavoura: "))
        comprimento_rua = float(input("Comprimento de cada rua em metros: "))

        total_metros_lineares = num_ruas * comprimento_rua
        total_insumo_unidade = total_metros_lineares * quantidade_por_metro  # em mL ou g

        # Se for <1000 exibe em mL/g; se >=1000 exibe em L/Kg (com 3 casas) e também em mL/g
        if total_insumo_unidade >= 1000:
            total_insumo_litros = total_insumo_unidade / 1000.0
            print(f"\nSerão necessários {total_insumo_litros:.3f} L/Kg de {produto} para a lavoura ({total_insumo_unidade:.0f} mL/g).")
        else:
            print(f"\nSerão necessários {total_insumo_unidade:.2f} mL/g de {produto} para a lavoura ({total_insumo_unidade/1000:.3f} L/Kg).")

        # armazenar em litros/kg para consistência
        total_insumo = total_insumo_unidade / 1000.0

    except ValueError:
        print("\n Entrada inválida para manejo de insumos. Por favor, digite números.")
        return