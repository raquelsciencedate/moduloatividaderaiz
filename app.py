from moduloatividade import * 

def exibir_menu():
    print("Menu:")
    print("1. Calcular potência")
    print("2. Calcular raiz quadrada")
    print("0. Sair")

# programa principal para proteger o código
if __name__ == "__main__":
    while True:
        exibir_menu()
        opcao = input("Opção desejada: ")

        match opcao:
            case "0":
                break
            case "1":
                numero = float(input("Informe um número: ").replace(",", "."))
                expoente = float(input("Informe o expoente: ").replace(",", "."))
                resultado = calcular_potencia(numero, expoente)
                print(f"A potência de {numero} elevado a {expoente} é {resultado}")
            case "2":
                numero = float(input("Informe um número: ").replace(",", "."))
                resultado = calcular_raiz_quadrada(numero)
                print(f"A raiz quadrada de {numero} é {resultado}")
            case _:
                print("Opção inválida. Tente novamente.")