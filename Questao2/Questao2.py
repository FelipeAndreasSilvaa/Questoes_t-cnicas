import time

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    return fib_sequence

def is_fibonacci_number(num):
    fib_sequence = fibonacci_sequence(num)
    return num in fib_sequence

# Entrada do usuário
numero = int(input("Informe um número: "))

print("Fazendo cálculo...")
time.sleep(1)  # Pausa por 1 segundo para simular o cálculo

if is_fibonacci_number(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
