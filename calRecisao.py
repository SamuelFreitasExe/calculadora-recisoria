# Cálculos Rescisórios Obrigatórios
print("-------------------------------Cálculos Rescisórios Obrigatórios-------------------------------")

# Recebe a entrada de salário e meses trabalhados
baseSalarial = input("Digite seu salário: ")
entrada = input("Digite o total de meses trabalhados: ")

# Substitui vírgula por ponto e converte para float
salario = float(baseSalarial.replace(",", "."))
mesesTrabalhados = float(entrada.replace(",", "."))

# Verifica se o salário é válido (positivo)
if salario > 0:
    fgts = salario * 0.08
    print(f"Valor mensal do FGTS (8%): {fgts:.2f}")
else:
    print("Erro: O salário deve ser maior que zero.")
    fgts = 0  # Define o FGTS como 0 em caso de erro

# Cálculos da multa rescisória, férias proporcionais e décimo terceiro
multaRecisoria = fgts * 0.40
fereiasProporcional = (mesesTrabalhados / 12) * salario
decimoTerceiro = (mesesTrabalhados / 12) * salario

# Exibe os valores dos cálculos
print(f"Valor da multa rescisória (40%): {multaRecisoria:.2f}")
print(f"Valor das férias proporcionais: {fereiasProporcional:.2f}")
print(f"Valor do décimo terceiro: {decimoTerceiro:.2f}")

# Cálculos de descontos
print("----------------------Cálculos de Descontos-----------------------------------")
impostoDeRenda = salario * 0.1133
inss = salario * 0.08
valeTransporte = salario * 0.06

# Exibe os descontos
print(f"Desconto de Imposto de Renda (11,33%): {impostoDeRenda:.2f}")
print(f"Desconto de INSS (8%): {inss:.2f}")
print(f"Desconto de Vale Transporte (6%): {valeTransporte:.2f}")

# Cálculo do valor total rescisório
print("------------------------Valor Total Rescisório-----------------------")
valorTotalRecisorio = fereiasProporcional + fgts + multaRecisoria + decimoTerceiro
print(f"O valor total rescisório: {valorTotalRecisorio:.2f}")

# Cálculo do valor líquido rescisório
print("------------------------Valor Líquido Rescisório-----------------------")
valorLiquidoRecisorio = valorTotalRecisorio - impostoDeRenda - inss - valeTransporte
print(f"O valor total líquido: {valorLiquidoRecisorio:.2f}")
