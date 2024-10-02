# Pedir para o usuário digitar uma string
minha_string = input("Digite uma string para inverter: ")

# Variável para armazenar a string invertida
string_invertida = ""

# Laço para percorrer a string de trás para frente
for i in range(len(minha_string) - 1, -1, -1):
    string_invertida += minha_string[i]  # Adicionar cada caractere à string invertida

#  Mostrar a string invertida
print("A string invertida é:", string_invertida)
