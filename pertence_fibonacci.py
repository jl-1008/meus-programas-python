# Programa para verificar se um número está na sequência de Fibonacci

# Função para calcular a sequência de Fibonacci e verificar o número
def pertence_fibonacci(n):
    # Começamos a sequência de Fibonacci com os dois primeiros números
    num1 = 0  # Primeiro número da sequência
    num2 = 1  # Segundo número da sequência
    
    # Enquanto o número atual for menor ou igual ao número dado
    while num1 <= n:
        if num1 == n:  # Se encontramos o número na sequência
            return True  # O número pertence à sequência
        # Aqui atualizamos os números para o próximo da sequência
        novo_numero = num1 + num2  # Soma dos dois últimos números
        num1 = num2  # Avançamos o primeiro número
        num2 = novo_numero  # Avançamos o segundo número

    return False  # Se saímos do laço, o número não pertence à sequência

# Pedir ao usuário para digitar um número
numero = int(input("Digite um número: "))

# Verificar se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} está na sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO está na sequência de Fibonacci.")
