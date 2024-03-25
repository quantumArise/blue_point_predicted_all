#!/usr/bin/env python

import sys

def Pn(Pp):
    Pn = 0.99 * Pp + 0.01
    return Pn

if len(sys.argv) != 2:
        print("Usage: Pn Pp")
        sys.exit(1)
Pp = float(sys.argv[1])

try:
        resultat = Pn(Pp)
        print(f"Le résultat est {resultat}")
except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
