class BuscaEndereco:
    def __init__(self,cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep invalido!!")

    def cep_e_valido(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def __str__(self):
        return self.format_cep()