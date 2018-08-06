#dados conhecidos - se e gordo, perna curta, late
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

#array com os dados ja conhecidos
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

#array com o resultado da classificacao dos dados que ja conhecemos
marcacoes = [1,1,1,-1,-1,-1]


#importar do sklearn o algoritmo bayesiano
from sklearn.naive_bayes import MultinomialNB

#criacao de um modelo para prever a classificacao dos elementos misteriosos
modelo = MultinomialNB()

#treinamento
modelo.fit(dados, marcacoes)

#elemento que nao sabemos o que e
misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]
testes = [misterioso1, misterioso2, misterioso3]

marcacoes_teste = [-1,1,-1]

#previsao
resultado = modelo.predict(testes)
print(resultado)

diferencas = resultado - marcacoes_teste


acertos = [d for d in diferencas if d==0]


total_de_acertos = len(acertos)

total_de_elementos = len(testes)


taxa_de_acerto = 100.0*total_de_acertos/total_de_elementos
print(taxa_de_acerto)
