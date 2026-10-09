import random
import time
import os

# --- Configurações do Jogo ---
LARGURA_PISTA = 40
ALTURA_PISTA = 15
LINHA_CHEGADA = 5  # Posição horizontal onde os bots vencem (próximo ao lado esquerdo)
VOLTAS_PARA_VENCER = 3


# --- Funções do Jogo ---
def criar_pista():
    pista = [[" " for _ in range(LARGURA_PISTA)] for _ in range(ALTURA_PISTA)]

    # Desenha a pista (linhas laterais)
    for y in range(ALTURA_PISTA):
        pista[y][0] = "|"
        pista[y][LARGURA_PISTA - 1] = "|"

    # Desenha a linha de chegada
    for y in range(ALTURA_PISTA):
        pista[y][LINHA_CHEGADA] = "-"

    return pista


# --- Classe para o Bot ---
class Bot:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.posicao = LARGURA_PISTA - 2  # Começa do lado direito
        self.voltas = 0

    def mover(self):
        # Diminui a posição do bot em um valor aleatório (1 a 3)
        self.posicao -= random.randint(1, 3)


# -- função para desenhar o jogo --
def desenharjogo(pista, bots):
    os.system("cls" if os.name == "nt" else "clear")

    pista_temporaria = [linha[:] for linha in pista]
    for i, bot in enumerate(bots):
        y_pos = 2 + (i * 3)
        x_pos = max(1, min(bot.posicao, LARGURA_PISTA - 2))
        if y_pos < ALTURA_PISTA:
            pista_temporaria[y_pos][x_pos] = bot.nome

    for linha in pista_temporaria:
        print("".join(linha))

    print("\n --- STATUS ---")
    for bot in bots:
        print(f"bot={bot.nome} ({bot.posicao}): {bot.voltas} voltas")


def verificar_vencedor(bots):
    for bot in bots:
        if bot.posicao <= LINHA_CHEGADA:
            bot.posicao = (
                LARGURA_PISTA - 2
            )  # Reseta a posição para a próxima volta (lado direito)
            bot.voltas += 1
            print(f"\n--- Bot {bot.nome} completou uma volta! ---")
            if bot.voltas >= VOLTAS_PARA_VENCER:
                print(f"\n🏆 Bot {bot.nome} venceu a corrida! 🏆")
                return True
    return False


# --- Lógica Principal do Jogo ---
def iniciar_corrida():
    bots = [Bot("🚗", "vermelho"), Bot("🚙", "azul")]
    pista = criar_pista()
    vencedor = False

    while not vencedor:
        desenharjogo(pista, bots)

        for bot in bots:
            bot.mover()

        time.sleep(0.5)  # Espera 0.5 segundos antes de atualizar a tela

        vencedor = verificar_vencedor(bots)


if __name__ == "__main__":
    iniciar_corrida()
