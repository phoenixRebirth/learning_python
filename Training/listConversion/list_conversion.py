import time

# créer la liste :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(range(0, 11))


# créer la liste :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] en utilisant les list
# comprehension
[elt for elt in range(0, 11)]

# créer la même liste mais en ne gardant que les termes pairs
[i for i in range(0, 11) if i%2==0]

# créer la liste de dictionnaires : [{0:pair}, {1: impair}, {2: pair},
# {3: impair}, ......, {10: pair}]
l = list(range(0, 11))
l = [{i: 'pair'} if i%2 == 0 else {i: 'impair' } for i in l]

# faire pareil en mettant la condition "i%2 == 0" dans une fonction
l = list(range(0, 11))
def condition(i):
    return i%2 == 0

l = [{i: 'pair'} if condition(i) else {i: 'impair' } for i in l]

# appliquer la fonction filter sur la liste : l = [i for i in range(0, 11)]
# rappel (signature de filter) : filter(lambda x : ..., le truc sur lequel on
# veut filtrer)
l = list(range(0, 11))
l = list(filter(lambda x: x%2 == 0, l))

# Créer le dictionnaire "d" suivant : {'client_8': 'pierre',
#'client_2': 'christophe', 'client_3': 'test'}
d = {'client_8': 'pierre', 'client_2': 'christophe', 'client_3': 'test'}


# à partir du dictionnaire "d", créer de deux manières différentes une liste
# contenant les valeurs du dictionnaire (utiliser d.items() pour la 2ème méthode)

l = [d[k] for k in d]
l = [k for k, v in d.items()]

# un "_" peut être utilisé pour éviter de le stocker en mémoire quand on en a
# pas besoin:

ts1 = time.time()
l = [k for k, _v in d.items()]
# print(time.time()-ts1)

ts1 = time.time()
l = [k for k, v in d.items()]
#print(time.time()-ts1)

# convertir le dictionnaire "d" en la liste suivante (une liste de dictionnaire
# de 2 éléments) :
# [
# {'num_client' : 'client_8', 'nom_client': pierre},
# {'num_client' : 'client_2', 'nom_client': christophe},
# {'num_client' : 'client_3', 'nom_client': test}
# ]

l = [{'num_client': k , 'nom_client': v} for k, v in d.items()]

##############################################################################
'''
 Ecrire la forme générale de création d'une liste à partir d'un autre liste
 (c'est à dire de manière factorisée)
 conseil : creer deux fonctions "transform" et "condition" et injecter les
 dans une list comprehension
 dans ce cas : la fonction "transform" renvoit k et prend l et k donc ne fait rien
 et la fonction "condition" renvoit que les nombres s'ils sont paires
'''
l = list(range(0,11))

def transform(k):
    return k

def condition (k):
    return k%2==0

l = [transform(k) for k in l if condition(k)]


##############################################################################
'''
dans ce cas faire une nouvelle liste qui renvoit:
[{0: 'pair'}, {1: 'impair'}, {2: 'pair'}, .... , {10: 'pair'}]
'''
l = list(range(0,11))

def transform(k):
    return {k , 'pair'} if k%2 == 0 else {k , 'impair'}

def condition (k):
    return True

l = [transform(k) for k in l if condition(k)]

##############################################################################
'''
créer un dictionnaire avec pour clef la position de l'élément dans la liste
et pour valeur la chaine de caractère à la position correspondante
'''
# {position(elt_list), valeur(elt_list)}
l = ['salut', 'ca', 'va', 'ou', 'pas']
d = {pos: value for pos, value in enumerate(l)}

##############################################################################
'''
écrire la forme générale (on doit avoir la possibilité de processer le i et
l'elt). Par exemple garder que les éléments avec un indice pair +
aux éléments vérifiants cette condition : multiplier par deux l'indice
en clef et passer en majuscule l'elt.
output : {0: 'SALUT', 4: 'VA', 8: 'PAS'}
'''
def process_1(pos):
    return pos*2

def process_2(value):
    return value.upper()

def condition (pos):
    return pos%2 == 0

d = {process_1(pos): process_2(value) for pos, value in enumerate(l) if condition(pos)}
print(d)

#############################################################################
'''
créer la matrice identité 10*10
'''
l = [[0 if i!=j else 1 for i in range(0,11)] for j in range(0, 11)]

'''
céer une matrice de 0 (10*10) avec une list comprehension
'''
l = [[0 for i in range(0,11)] for j in range(0, 11)]

'''
créer la matrice identité 10*10 avec une list comprehension
'''


################################################################################

# transformer une chaine de caractère en tableau et l'inverse
ma_string = 'salut moi c\'est Colin alias le furet'
l = ma_string.split(' ')
print(l)
l = " ".join(l)
print(l)

# l1 et l2 sont 2 variables différentes qui représentent la même liste (même case mémoire)
# donc quand on retire un élément d'une des deux listes, cela supprime dans les 2 listes

# il faut distinguer les structures (ici listes) de ce qu'elles contiennent (les différents éléments, ici des dictionnaires)
# l1 et l2 sont 2 variables différentes qui représentent 2 listes différentes initialement avec les mêmes éléments
d1 = { 'name': 'christophe'}            # 1
d2 = { 'name': 'pierre'}                # 2
l1 = [d1, d2]                           # 3 [1, 2]
l2 = [elt for elt in l1]                # 4 [1, 2]
l2.remove(d1)                           # 4 [2]
print(l1, l2)

l2[0]['name'] = 'autre'                 # 2['name'] = 'autre'
print(l1, l2)
print(d2)
#print('')

# l1 et l2 sont 2 variables différentes qui représentent 2 listes différentes contenant des éléments différents mais de contenu identique
import copy
d1 = { 'name': 'christophe'}            # 1
d2 = { 'name': 'pierre'}                # 2
l1 = [d1, d2]                           # 3 [1, 2]
l2 = copy.deepcopy(l1)                  # 4 [5, 6]

#print(l1, l2)

l2[0]['name'] = 'autre'                 # 5['name'] = 'autre'
#print(l1, l2)

# modifier uniquement les éléments d'une liste vérifiants une condition donnée:
d1 = { 'name': 'christophe', 'type': 0, 'score': 5}
d2 = { 'name': 'pierre', 'type': 1, 'score': 18}
l1 = [d1, d2]
l2 = [elt for elt in l1 if elt['type'] == 1]
for elt in l2:
    elt['score'] += 1
# print(l1)


# avec les objects en python, on affecte la référence
d1 = {'name': 'christophe'}
d2 = d1
d2['name'] = 'pierre'
print('\n\n\n\n')
print(d1, d2)

# avec les types primitifs, on ne donne une référence mais une copie (affecte la valeur
# mais pas la refference)
i = 4
j = i
j = 5
print(i, j)


##############################################################################
