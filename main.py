class MaquinaNorma:
    def __init__(self, A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0):
        # Inicializa os registradores com os valores fornecidos ou 0 por padrão
        self.registradores = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H}

    def add(self, reg):
        """Incrementa o valor do registrador em 1."""
        self.registradores[reg] += 1

    def sub(self, reg):
        """Decrementa o valor do registrador em 1, se não for zero."""
        if self.registradores[reg] > 0:
            self.registradores[reg] -= 1

    def zer(self, reg):
        """Verifica se o valor do registrador é zero."""
        return self.registradores[reg] == 0

    def execute_instruction(self, instruction):
        """Executa uma instrução e retorna o índice de salto."""
        parts = instruction.split()
        if len(parts) < 2:
            return None

        label, cmd, reg, *jumps = parts

        if cmd == 'ADD':
            self.add(reg)
            return int(jumps[0])
        elif cmd == 'SUB':
            self.sub(reg)
            return int(jumps[0])
        elif cmd == 'ZER':
            if self.zer(reg):
                return int(jumps[0])
            else:
                return int(jumps[1])
        else:
            return None

    def get_register_values(self):
        """Retorna os valores atuais dos registradores."""
        return tuple(self.registradores.values())

    def executar_programa(self, program):
        """Executa um programa de instruções."""
        i = 0
        while i < len(program):
            current_state = self.get_register_values()
            print(f"{current_state} , {i + 1}) {program[i]}")
            i = self.execute_instruction(program[i]) - 1

    def initialize_registers(self, values):
        """Inicializa os registradores com valores específicos."""
        for reg, value in values.items():
            if reg in self.registradores:
                self.registradores[reg] = value
            else:
                print(f"Registrador {reg} não existe.")


# Funções auxiliares para macros
def soma(maquina, reg_a, reg_b):
    """Realiza a soma A := A + B."""
    program = [
        "1 ADD A 2",
        "2 SUB B 1",
        "3 ZER B 4 2",
        "4 ADD A 5",
        "5 ZER B 6 3",
        "6 ZER B 7 7"
    ]
    maquina.executar_programa(program)

def multiplicacao(maquina, reg_a, reg_b, reg_c):
    """Realiza a multiplicação A := A * B usando C como auxiliar."""
    program = [
        "1 ZER C 2 3",
        "2 ZER B 7 4",
        "3 ADD C 4",
        "4 SUB B 1",
        "5 ADD A 6",
        "6 SUB C 2",
        "7 ZER C 8 8"
    ]
    maquina.executar_programa(program)

def fatorial(maquina, reg_a, reg_b, reg_c):
    """Calcula o fatorial de A, armazenando o resultado em B."""
    program = [
        "1 ZER B 2 3",
        "2 ADD B 4",
        "3 ZER A 8 5",
        "4 SUB A 6",
        "5 ZER C 7 6",
        "6 ADD C 3",
        "7 ZER C 8 8"
    ]
    maquina.executar_programa(program)


# Função para carregar o programa de um arquivo
def read_program(file_path):
    """Carrega as instruções de um arquivo."""
    with open(file_path, 'r') as file:
        program = file.readlines()
    return [line.strip() for line in program]


# Função principal
def main():
    print("Máquina de Norma")
    while True:
        print("Menu:")
        print("1 - Somar")
        print("2 - Multiplicar")
        print("3 - Fatorial")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            print("Soma")
            program = read_program('soma.txt')
            A = int(input("Valor inicial de A: "))
            B = int(input("Valor inicial de B: "))
            C = 0
            D = 0
            maquina = MaquinaNorma(A, B, C, D)
            maquina.executar_programa(program)
        elif opcao == 2:
            print("Multiplicação")
            program = read_program('multiplicacao.txt')
            A = int(input("Valor inicial de A: "))
            B = int(input("Valor inicial de B: "))
            C = 0
            D = 0
            maquina = MaquinaNorma(A, B, C, D)
            maquina.executar_programa(program)
        elif opcao == 3:
            print("Fatorial")
            program = read_program('fatorial.txt')
            A = int(input("Valor inicial de A: "))
            B = 0
            C = 0
            D = 0
            maquina = MaquinaNorma(A, B, C, D)
            maquina.executar_programa(program)
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
