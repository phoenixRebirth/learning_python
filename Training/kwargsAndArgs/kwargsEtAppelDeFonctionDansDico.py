import sys

print("***********************************************************************")

def f(**kwargs):
    print('kwargs est un dictionnaire : ' + str(kwargs))
    if kwargs.get("nom", {}) == {}:
        print("ya pas de kwargs")
    else:
        nom = kwargs.get("nom", {})
        print(nom)

f(nom='cong', prenom='Colin')

d = {'nom': 'Cong', 'prenom': 'Colin'}
f(**d)

f()

print("\n*******************************************************************")
def g(arg1=3, **kwargs):
    print(arg1)

def h(**kwargs):
    print("toto")

def i(**kwargs):
    print("tata")

d = {
'g': lambda x : g(**x),
'h' : lambda x : h(**x),
'i' : lambda x : i(**x)
}

d['g']({'com' : 'Colin', 'age' : 'lfksfhg'})
d['g']({})

print("\n**********************************************************************")

d = {
'g': g(**{'com' : 'Colin', 'age' : 'lfksfhg'}),
'h' : h,
'i' : i()
}

print(d['g'])

print("\n**********************************************************************")

d = {
'g': g,
'h' : h,
'i' : i()
}

if len(sys.argv) == 2:
    d['g'](arg1 = sys.argv[1], **{'com' : 'Colin', 'age' : 'lfksfhg'})

d['g'](**{'com' : 'Colin', 'age' : 'lfksfhg'})

d['h']()

d = {
'f': lambda x : print(x*2),
'g': lambda y : print(y*2)
}
