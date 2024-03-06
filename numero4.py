import random

def associar_interruptores_lampadas():
    # Inicializa as lâmpadas e interruptores
    lampadas = [1, 2, 3]
    interruptores = [1, 2, 3]

    print("Associação inicial:")
    for i in range(3):
        print(f"Lâmpada {lampadas[i]} está associada ao Interruptor {interruptores[i]}")

    # Associa aleatoriamente os interruptores às lâmpadas
    random.shuffle(lampadas)
    random.shuffle(interruptores)

    print("\nAssociação aleatória:")
    for i in range(3):
        print(f"Lâmpada {lampadas[i]} está associada ao Interruptor {interruptores[i]}")

    # Simula o processo de acender as lâmpadas
    for i in range(2):
        interruptor_acendido = random.choice(interruptores)
        lampada_acendida = lampadas.pop(0)

        print(f"\nAcendendo Interruptor {interruptor_acendido}... Lâmpada {lampada_acendida} acendeu.")
        print(f"Lâmpada {lampada_acendida} está associada ao Interruptor {interruptor_acendido}\n")

        # Remove o interruptor associado à lâmpada acendida
        interruptores.remove(interruptor_acendido)

    # Associa automaticamente o interruptor e lâmpada restantes
    interruptor_final = interruptores[0]
    lampada_final = lampadas[0]

    print(f"\nAssociação automática: Lâmpada {lampada_final} está associada ao Interruptor {interruptor_final}")
    print("\nAssociações concluídas!")

# Executa a função para associar os interruptores às lâmpadas
associar_interruptores_lampadas()




