#!/usr/bin/env python

import sys

def Sn(Sp):
    Sn = 0.96 * Sp - 17.63
    return Sn

if len(sys.argv) != 2:
        print("Usage: Sp Sn")
        sys.exit(1)
Sp = float(sys.argv[1])

try:
        resultat = Sn(Sp)
        print(f"Le résultat est {resultat}")
except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
