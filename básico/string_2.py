nome = "Jonas"
idade = 40
profissão = "Programador"
linguagem = "Python"

dados = {"nome": "Jonas", "idade": 40 }

print("nome: %s idade: %i" % (nome, idade))
print("nome: {} idade: {}".format(nome, idade))
print("nome: {0} idade: {1}".format(nome, idade))
print("idade: {1} nome: {0} idade: {1}".format(nome, idade))
print("nome: {nome} idade: {idade}".format(idade=idade, nome=nome))
print("nome: {nome} idade: {idade}".format(**dados))

print(f"nome: {nome} idade: {idade}")