#!/usr/bin/env python

import sys

def Ep(En):
    Ep =  (En - 1.91)/1.01
    return Ep

if len(sys.argv) != 2:
        print("Usage: Ep En")
        sys.exit(1)
En = float(sys.argv[1])

try:
        resultat = Ep(En)
        print(f"Le résultat est {resultat}")
except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
