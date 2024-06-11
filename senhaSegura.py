class Senha:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def tamanhoSenha(self):
        if len(self.conteudo) >= 10 and len(self.conteudo) <= 30:
            pass
        else:
            return "A senha deverá ter entre 10 a 30 caracteres"

    def letrasNaSenha(self):
        if any(x.isupper() for x in self.conteudo) and any(x.islower() for x in self.conteudo):
            return self.conteudo
        else:
            return "A senha deverá ter uma letra minúscula e uma letra maiúscula para ser segura"

    def numeroNaSenha(self):
        if any(x.isdigit()for x in self.conteudo):
            return self.conteudo
        else:
            return "A senha deverá ter um número para ser segura"

    def forçaSenha(self):
        repetido = 0
        letras = []

        for letra in self.conteudo:
            if letra not in letras:
                letras.append(letra)
            else:
                repetido += 1

        if len(self.conteudo) >= 10:
            return ("Sua senha está minimamente segura: ", 75 - repetido)
        elif len(self.conteudo) >= 20:
            return ("Sua senha está minimamente segura: 90", 90 - repetido)
        else:
            return ("Sua senha está minimamente segura: 100", 100 - repetido)
    # def alteracaoSenha(self):


sen = Senha("Senha12345678")

print(sen.forçaSenha())
