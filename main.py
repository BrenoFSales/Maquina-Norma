class NormaMachine:
    # Inicializa 8 registradores
    def __init__(self):
        self.registers = {reg: 0 for reg in "ABCDEFGH"}

    # Define o valor inicial de um registrador
    def set_register(self, reg, value):
        if reg in self.registers:
            self.registers[reg] = value

    # Retorna o valor de um registrador
    def get_register(self, reg):
        return self.registers.get(reg, None)

    # Incrementa o valor de um registrador
    def add(self, reg):
        if reg in self.registers:
            self.registers[reg] += 1

    # Decrementa o valor de um registrador se ele for maior que 0
    def sub(self, reg):
        if reg in self.registers and self.registers[reg] > 0:
            self.registers[reg] -= 1

    # Testa se o registrador contém zero
    def test_zero(self, reg):
        return self.registers[reg] == 0 if reg in self.registers else False

# -------------------------------------------------------------------------- #
def main():
    
    print("Executar o código aqui!")

if __name__ == "__main__":
    main()