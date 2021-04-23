

from pyswip import *


def teste():
    p = Prolog()

    assertz = Functor("assertz")
    pai_fun = Functor("pai", 2)
    mae_fun = Functor("mae", 2)
    fun_mulher = Functor("mulher", 1)
    fum_homem = Functor("Homem", 1)
    test1 = newModule("test1")
    test2 = newModule("test2")

    call(assertz(pai_fun("marcos", "marcus")), module=test1)
    call(assertz(mae_fun("jane", "bob")), module=test1)
    

    call(assertz(pai_fun("mike", "bob")), module=test2)
    call(assertz(pai_fun("gina", "bob")), module=test2)

    print("knowledgebase test1")

    X = Variable()
    q = Query(pai_fun(X, "marcus"), module=test1)
    while q.nextSolution():
        print(X.value)
    q.closeQuery()

    print("knowledgebase test2")

    q = Query(pai_fun(X, "marcus"), module=test2)
    while q.nextSolution():
        print(X.value)
    q.closeQuery()

def nome_sexo():
    p = Prolog()
    var = Variable()
    print('insira o nome')
    nome = input()
    print('insira o sexo?')
    sexo = input()
    assertz = Functor("assertz")
    fun_homem = Functor('homem')
    modulo = newModule("modulo")
    a = call(assertz(fun_homem(nome)))
    
    X = Variable()
    q = Query(fun_homem(X, "marcus"))
    while q.nextSolution():
        print(X.value)
    q.closeQuery()


def main():
    print('me fale seu nome')
    nome_sexo()

    
if __name__ == "__main__":
    main()

