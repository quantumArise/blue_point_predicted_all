#!/usr/bin/env python

import sys

def Sp(Sn):
    Sp =  ( Sn + 17.63)/0.96
    return Sp

if len(sys.argv) != 2:
        print("Usage: Sp Sn")
        sys.exit(1)
Sn = float(sys.argv[1])

try:
        resultat = Sp(Sn)
        print(f"Le résultat est {resultat}")
except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
