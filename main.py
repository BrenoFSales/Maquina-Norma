class MaquinaNorma:
    def __init__(self):
        # Inicializando os registradores com valor zero
        self.registradores = {reg: 0 for reg in "ABCDEFGH"}
    
    #INICIALIZA REGISTRADORES
    def inicializar_registradores(self, valores):
        """Inicializa os registradores com os valores fornecidos."""
        for reg, valor in valores.items():
            if reg in self.registradores:
                self.registradores[reg] = valor
            else:
                print(f"Registrador {reg} não existe.")

    #FUNÇÃO DE SOMA
    def ADD(self, reg):
        """Incrementa o valor do registrador em 1."""
        self.registradores[reg] += 1

    #FUNÇÃO DE SUBTRAÇÃO
    def SUB(self, reg):
        """Decrementa o valor do registrador em 1, se não for zero."""
        if self.registradores[reg] > 0:
            self.registradores[reg] -= 1
        else:
            print(f"Erro: Tentativa de decrementar registrador {reg} que já está em zero.")

    #FUNÇÃO DE VERIFICAÇÃO DE VALOR - ZERO
    def ZER(self, reg):
        """Verifica se o registrador contém o valor zero."""
        return self.registradores[reg] == 0

    #EXECUÇÃO DO PROGRAMA
    def executar_programa(self, instrucoes):
        """Executa um conjunto de instruções."""
        i = 0
        while i < len(instrucoes):
            instrucao = instrucoes[i]
            operacao = instrucao[0]
            reg = instrucao[1]

            if operacao == "ADD":
                self.ADD(reg)
            elif operacao == "SUB":
                self.SUB(reg)
            elif operacao == "ZER":
                if not self.ZER(reg):
                    print(f"Registrador {reg} não é zero.")
            elif operacao == "JMP":
                i = int(reg) - 1  # Ajuste de índice para a lista
                continue
            elif operacao == "PRINT":
                print(f"Registrador {reg}: {self.registradores[reg]}")
            else:
                print(f"Operação desconhecida: {operacao}")

            i += 1

    #EXIBIR REGISTRADORES
    def exibir_registradores(self):
        """Exibe os valores dos registradores."""
        print("Estado dos registradores:")
        for reg, valor in self.registradores.items():
            print(f"{reg}: {valor}")


# Lendo o arquivo de entrada
def carregar_programa(arquivo):
    """Carrega as instruções de um arquivo."""
    instrucoes = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.strip().split()
                if len(partes) == 2:  # Exemplo: ADD A
                    instrucoes.append((partes[0], partes[1]))
                elif len(partes) == 1:  # Exemplo: JMP 4
                    instrucoes.append((partes[0],))
                else:
                    print(f"Instrução inválida: {linha}")
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
    return instrucoes


# -------------------------------------------------------------------------- #
def main():
    
    print("Executar o código aqui!")

if __name__ == "__main__":
    main()