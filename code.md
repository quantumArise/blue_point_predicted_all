![Screensho](https://github.com/quantumArise/blue_point_predicted_all/assets/162140361/2cfadc74-5c92-444f-901c-be72c5deddf1)

## Calcul d'En avec Python
Ce script Python permet de calculer En en fonction de Ep à l'aide de la formule suivante :

En = 1.01 * Ep + 1.91
## Calcul d'Ep avec Python
Ce script Python permet de calculer Ep en fonction de En à l'aide de la formule suivante :

```Ep = (En - 1.91) / 1.01``
## Calcul de Pn avec Python
Ce script Python permet de calculer Pn en fonction de Pp à l'aide de la formule suivante :
```Pn = 0.99 * Pp + 0.01```
## Calcul de Pp avec Python
Ce script Python permet de calculer Pp en fonction de Pn à l'aide de la formule suivante :
```Pp = (Pn - 0.01) / 0.99```
## Calcul de Sn avec Python
Ce script Python permet de calculer Sn en fonction de Sp à l'aide de la formule suivante :
```Sn = 0.96 * Sp - 17.63```
## Calcul de Sp avec Python
Ce script Python permet de calculer Sp en fonction de Sn à l'aide de la formule suivante :
```Sp = (Sn + 17.63) / 0.96```
# Exemple d'utilisation
Assurez-vous d'avoir Python installé sur votre système. Vous pouvez exécuter le script en utilisant la commande suivante :

```python En [Ep]```

où [Ep] est à utiliser pour le calcul.

Si aucun argument n'est fourni ou si l'argument n'est pas un nombre valide, le script affichera un message d'erreur indiquant l'utilisation correcte.


```python En.py 10.5``` 
Ce qui produira la sortie suivante :


```Le résultat est 12.115```


## Auteur

Ce script a été écrit par Delchere Dontsa dans le cadre d'un projet de recherche en Physique
