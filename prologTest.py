# -*- coding:utf-8 -*-
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("parent(vincent,arthur)")
prolog.assertz("parent(michael,arthur)")
prolog.assertz("parent(michael,alan)")
prolog.assertz("parent(robert,alan)")

query=prolog.query("parent(X,arthur)")
for solution in query:
    print(solution)

query=prolog.query("parent(X,Y)")
for solution in query:
    print(solution)