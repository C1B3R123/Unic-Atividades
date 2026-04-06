# Aqui coloquei apenas a classe do aluno para simplificar e organizar o código
class Aluno:
    def __init__(self, nome, matricula, curso, id=None):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
