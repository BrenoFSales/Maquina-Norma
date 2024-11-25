class MaquinaNorma:
    def __init__(self):
        # Inicializando os registradores com valor zero
        self.registradores = {reg: 0 for reg in "ABCDEFGH"}

    def inicializar_registradores(self, valores):
        """Inicializa os registradores com os valores fornecidos."""
        for reg, valor in valores.items():
            if reg in self.registradores:
                self.registradores[reg] = valor
            else:
                print(f"Registrador {reg} não existe.")

    def ADD(self, reg):
        """Incrementa o valor do registrador em 1."""
        self.registradores[reg] += 1

    def SUB(self, reg):
        """Decrementa o valor do registrador em 1, se não for zero."""
        if self.registradores[reg] > 0:
            self.registradores[reg] -= 1
        else:
            print(f"Erro: Tentativa de decrementar registrador {reg} que já está em zero.")

    def ZER(self, reg, jump_zero, jump_nonzero):
        """Testa se o registrador contém zero e retorna o rótulo para onde deve pular."""
        return jump_zero if self.registradores[reg] == 0 else jump_nonzero

    def executar_programa(self, instrucoes):
        """Executa as instruções lidas de um arquivo."""
        posicao = 0
        while posicao < len(instrucoes):
            linha, operacao, reg, *jumps = instrucoes[posicao]
            if operacao == "ADD":
                self.ADD(reg)
                posicao = int(jumps[0]) - 1
            elif operacao == "SUB":
                self.SUB(reg)
                posicao = int(jumps[0]) - 1
            elif operacao == "ZER":
                posicao = self.ZER(reg, int(jumps[0]) - 1, int(jumps[1]) - 1)
            else:
                print(f"Operação desconhecida: {operacao}")
                break

    def exibir_registradores(self):
        """Exibe os valores dos registradores."""
        print("Estado dos registradores:")
        for reg, valor in self.registradores.items():
            print(f"{reg}: {valor}")


# Funções auxiliares para macros
def soma(maquina, reg_a, reg_b, reg_c):
    """Realiza a soma A := A + B usando C."""
    programa = [
        (1, "ZER", reg_a, 2, 4),  # Verifica se A é zero, vai para linha 2 se for
        (2, "ADD", reg_c, 3),     # Incrementa C
        (3, "SUB", reg_a, 1),     # Decrementa A
        (4, "ZER", reg_b, 5, 7),  # Verifica se B é zero, vai para linha 5 se for
        (5, "ADD", reg_c, 6),     # Incrementa C
        (6, "SUB", reg_b, 4),     # Decrementa B
        (7, "ZER", reg_c, 8, 9),  # Zera A e B
        (8, "ADD", reg_a, 10),
        (9, "ADD", reg_b, 10)
    ]
    maquina.executar_programa(programa)

def multiplicacao(maquina, reg_a, reg_b, reg_c, reg_d):
    """Realiza a multiplicação A := A * B usando C e D."""
    programa = [
        (1, "ZER", reg_c, 2, 4),  # Garante que C está zerado
        (2, "ADD", reg_c, 3),     # Incrementa C
        (3, "SUB", reg_a, 4),     # Decrementa A
        (4, "ZER", reg_a, 5, 2),  # Se A é zero, vai para linha 5
        (5, "ZER", reg_d, 6, 7),  # Garante que D está zerado
        (6, "ADD", reg_d, 8),     # Incrementa D
        (7, "SUB", reg_c, 5),     # Decrementa C
        (8, "ZER", reg_c, 9, 6),  # Se C é zero, multiplica
        (9, "ZER", reg_b, 10, 11), # Restaura B
        (10, "ADD", reg_b, 11),
    ]
    maquina.executar_programa(programa)

def fatorial(maquina, reg_a, reg_b, reg_c, reg_d):
    """Calcula o fatorial de A, armazenando o resultado em A."""
    programa = [
        (1, "ZER", reg_b, 2, 3),   # Zera B
        (2, "ADD", reg_b, 3),      # Define B = 1 (início do cálculo)
        (3, "ZER", reg_c, 4, 5),   # Zera C
        (4, "ADD", reg_c, 6),      # Incrementa C para multiplicação
        (5, "ZER", reg_d, 7, 8),   # Zera D
        (6, "SUB", reg_a, 9),      # Decrementa A
        (7, "ZER", reg_a, 10, 4),  # Se A é zero, finaliza
        (8, "ZER", reg_d, 11, 12), # Garante multiplicação limpa
        (9, "ADD", reg_d, 10),     # Incrementa D
        (10, "ADD", reg_a, 11),    # Atualiza o resultado final
    ]
    maquina.executar_programa(programa)


    


# Carregar o programa de um arquivo
def carregar_programa(arquivo):
    """Carrega as instruções de um arquivo."""
    instrucoes = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.strip().split()
                if len(partes) >= 3:  # Exemplo: 1 ADD A 2
                    rótulo = int(partes[0])
                    operacao = partes[1]
                    reg = partes[2]
                    jumps = partes[3:]
                    instrucoes.append((rótulo, operacao, reg, *jumps))
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
    return instrucoes


# Exemplo de uso
if __name__ == "__main__":
    # Inicializar a máquina
    maquina = MaquinaNorma()

    # Definir valores iniciais dos registradores
    valores_iniciais = {"A": 5, "B": 3, "C": 0, "D": 0}
    maquina.inicializar_registradores(valores_iniciais)

    # Carregar o programa de um arquivo
    arquivo_programa = "programa.txt"  # Substituir pelo caminho do arquivo
    instrucoes = carregar_programa(arquivo_programa)

    # Executar o programa
    maquina.executar_programa(instrucoes)

    # Exibir os registradores ao final
    maquina.exibir_registradores()
