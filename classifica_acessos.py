from dados import carregar_acessos
X,Y = carregar_acessos()

#Testar a funcao
#print(Y)
#print(X)

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(X,Y)
