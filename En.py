#!/usr/bin/env python

import sys

def En(Ep):
    En = 1.01 * Ep + 1.91
    return En

if len(sys.argv) != 2:
        print("Usage: En Ep")
        sys.exit(1)
Ep = float(sys.argv[1])

try:
        resultat = En(Ep)
        print(f"Le résultat est {resultat}")
except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
