class Alunos:
    def __init__(self, documento, nome, matricula, curso):
        self.documento = documento
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo

class Professor:
    def __init__(self, nome, disciplina, siape, curso):
        self.nome = nome
        self.disciplina = disciplina
        self.siape = siape
        self.curso = curso

