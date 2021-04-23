
from pyswip import *
from pyswip.easy import *

prolog = Prolog()

homem = prolog.assertz('homem(X)')
prolog.assertz('homem(maurizio)')
prolog.assertz('pai(X)')
alo = prolog.assertz('mãe(lucesia, helena)')
var = prolog.assertz('pai(maurizio, helena)')
prolog.assertz('mulher(helena)')
prolog.assertz('mulher(lucesia)')
prolog.assertz('homem(maurizio)')
pai = Functor('pai(Pai, Filho)')

b = print((bool(prolog.query('pai(maurizio, helena)'))))
if b == var:
    print('certo')
else:
    print('errado')

b = print((bool(prolog.query('homem(maurizio)'))))
if b == homem:
    print('certo')
else:
    print('errado')