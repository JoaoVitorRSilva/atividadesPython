from cadastro import Alunos, Curso, Professor

ads = Curso("ADS", "Manha")
biologia = Curso("LCB", "Manha")
agronomia = Curso("Agronomia", "Integral")

aluno_jao = Alunos("05455456546", "Jão", "05456", ads)
aluno_francis = Alunos("565465495", "Francis", "78921", agronomia)
aluno_lucas = Alunos("31358788", "Lucas", "4589", biologia)

profiuri = Professor("Iuri", "Programação", "545", ads)
profmaisa = Professor("Maisa", "Inglês", "789", agronomia)
profluis = Professor("Luis", "Redes", "789", biologia)

print (profiuri.curso.nome)
