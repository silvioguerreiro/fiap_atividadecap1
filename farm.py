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

    # Armazena dados no vetor
    dados_cultura = {
        "cultura": cultura,
        "area": area,
        "produto": produto,
        "total_insumo_unidade": total_insumo_unidade,  # mL/g
        "total_insumo_litros": total_insumo_unidade / 1000,  # L/Kg
        "figura_geometrica": figura_geometrica
    }
    culturas_data[cultura].append(dados_cultura)
    print("\nDados inseridos com sucesso!")

def saida_dados(cultura_selecionada=None):
    print("\n= Saída de Dados =")
    if not culturas_data["soja"] and not culturas_data["milho"]:
        print("Nenhum dado cadastrado ainda.")
        return

    culturas_a_exibir = [cultura_selecionada] if cultura_selecionada else culturas_data.keys()

    for cultura in culturas_a_exibir:
        if cultura in culturas_data and culturas_data[cultura]:
            print(f"\nDados para {cultura.capitalize()}:")
            for i, dados in enumerate(culturas_data[cultura]):
                print(f"  Registro {i+1}:")
                print(f"    Figura Geométrica: {dados["figura_geometrica"].capitalize()}")
                print(f"    Área de Plantio: {dados["area"]:.2f} m²")
                print(f"    Produto Utilizado: {dados["produto"]}")
                print(f"    Total de Insumo: {dados["total_insumo_unidade"]:.2f} mL/g "
                      f"({dados["total_insumo_litros"]:.3f} L/Kg)")

def atualizar_dados():
    print("\n--- Atualização de Dados ---")
    cultura = escolher_cultura()
    if not cultura:
        return

    if not culturas_data[cultura]:
        print(f"Nenhum dado cadastrado para {cultura} ainda.")
        return

    saida_dados(cultura) # Passa a cultura selecionada para a função de saída
    try:
        indice = int(input(f"\nDigite o número do registro para {cultura} que deseja atualizar: ")) - 1
        if 0 <= indice < len(culturas_data[cultura]):
            print(f"Atualizando Registro {indice+1} para {cultura.capitalize()}:")
            
            nova_area = input(f"Nova área de plantio (atual: {culturas_data[cultura][indice]["area"]:.2f} m²), deixe em branco para manter: ")
            if nova_area:
                culturas_data[cultura][indice]["area"] = float(nova_area)

            novo_produto = input(f"Novo produto (atual: {culturas_data[cultura][indice]["produto"]:.2f} m²), deixe em branco para manter: ")
            if novo_produto:
                culturas_data[cultura][indice]["produto"] = novo_produto

            novo_total_insumo = input(f"Novo total de insumo (atual: {culturas_data[cultura][indice]["total_insumo_unidade"]:.2f} Litros/Kg), deixe em branco para manter: ")
            if novo_total_insumo:
                culturas_data[cultura][indice]["total_insumo_unidade"] = float(novo_total_insumo)

            print("Dados atualizados com sucesso!")
        else:
            print("Índice de registro inválido.")
    except ValueError:
        print("\n Entrada inválida. Por favor, digite um número para o índice.")

def deletar_dados():
    print("\n--- Exclusão de Dados ---")
    cultura = escolher_cultura()
    if not cultura:
        return

    if not culturas_data[cultura]:
        print(f"Nenhum dado cadastrado para {cultura} ainda.")
        return

    saida_dados()
    try:
        indice = int(input(f"Digite o número do registro para {cultura} que deseja deletar: ")) - 1
        if 0 <= indice < len(culturas_data[cultura]):
            del culturas_data[cultura][indice]
            print("Registro deletado com sucesso!")
        else:
            print("Índice de registro inválido.")
    except ValueError:
        print("\n Entrada inválida. Por favor, digite um número para o índice.")

def exportar_dados_csv():
    print("\n= Exportando Dados para CSV =")
    if not culturas_data["soja"] and not culturas_data["milho"]:
        print("Nenhum dado para exportar.")
        return

    # 1. Prepara os dados para exportação
    dados_para_exportar = []
    for cultura, dados_list in culturas_data.items():
        for dados in dados_list:
            registro_formatado = {
                "Cultura": dados["cultura"].capitalize(),
                "Figura Geométrica": dados["figura_geometrica"].capitalize(), 
                "Área (m²)": dados["area"],
                "Produto Utilizado": dados["produto"],
                "Total Insumo (mL ou g)": dados["total_insumo_unidade"],
                "Total Insumo (L ou Kg)": dados["total_insumo_litros"]
            }
            dados_para_exportar.append(registro_formatado)

    if not dados_para_exportar:
        print("Nenhum dado para exportar.")
        return

    csv_file_name = "Relatorio_Farm.csv"
    full_path = os.path.abspath(csv_file_name)

    try:
        keys = dados_para_exportar[0].keys()
        
        # Compatibilidade para caracteres especiais
        with open(full_path, 'w', newline='', encoding='utf-8-sig') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys, delimiter=';')
            dict_writer.writeheader()
            dict_writer.writerows(dados_para_exportar)
        
        print(f"\nDados exportados com sucesso!")
        print(f"O arquivo foi salvo em: {full_path}")

    except PermissionError:
        print(f"\n[ERRO] Permissão negada para salvar o arquivo.")
        print(f"Verifique se o arquivo '{full_path}' não está aberto no Excel ou outro programa.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado ao exportar o arquivo: {e}")


# Item e.
def menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualização de dados")
    print("4. Deleção de dados")
    print("5. Exportar dados para CSV")
    print("6. Sair do programa")

    choice = input("\nEscolha uma opção: ")
    return choice

def main():
    while True:
        choice = menu_principal()

        if choice == '1':
            entrada_dados()
        elif choice == '2':
            saida_dados()
        elif choice == '3':
            atualizar_dados()
        elif choice == '4':
            deletar_dados()
        elif choice == '5':
            exportar_dados_csv()
        elif choice == '6':
            print("Programa encerrado")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()