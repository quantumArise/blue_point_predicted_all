#!/usr/bin/env python

import sys

def Pp(Pn):
    Pp =  (Pn - 0.01)/0.99
    return Pp

if len(sys.argv) != 2:
        print("Usage: Pp Pn")
        sys.exit(1)
Pn = float(sys.argv[1])

try:
        resultat = Pp(Pn)
        print(f"Le résultat est {resultat}")
except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
