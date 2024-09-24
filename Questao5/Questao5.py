# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Entrada do usuário
entrada = input("Informe uma string para inverter: ")

# Inverter a string
resultado = inverter_string(entrada)

# Exibir o resultado
print(f"String invertida: {resultado}")
