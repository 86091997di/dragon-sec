# Simula um vazamento de memória (Majin Buu devorando RAM)

leak = []

while True:
    leak.append("MajinBuu" * 10**6)  # consome memória sem parar
