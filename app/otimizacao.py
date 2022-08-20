from scipy.optimize import linprog
from app.models import Produto
lucro = []
fertilizantes = []
trabalhadores = []
quantidadeDeHectares = []
for p in Produto.objects.all():
    # realizamos um print com o nome do usuário para tal cadastro.
    # note que essa poderia ser qualquer outra operação, onde o atributo `user` fosse acessado
    print(p.nome)
    print(p.lucro)
    print("trabalhadores", p.trabalhadores)
    print("fertilizantes", p.fertilizantes)
    lucro.append(-p.lucro)
    fertilizantes.append(p.fertilizantes)
    trabalhadores.append(p.trabalhadores)
    quantidadeDeHectares.append(1)

lucroPorProcessador = [lucro] #Lucro por Trigo/Milho
print(trabalhadores)
print(fertilizantes)
print(lucro)
print(quantidadeDeHectares)

quantidadeParaProduzir1Item= [
quantidadeDeHectares,
trabalhadores,
fertilizantes
]

totalDeCadaItem = [
450,
1000,
1200 #Total de Trabalhadores disponiveis
] #Total de Fertilizantes disponiveis

resultado = linprog(
c=lucroPorProcessador,
A_ub=quantidadeParaProduzir1Item,
b_ub=totalDeCadaItem,
method="revised simplex")



