def remplacer_caractere(chaine, ancien_caractere, nouveau_caractere):
    return chaine.replace(ancien_caractere, nouveau_caractere)

chaine = input("Entrez une chaîne de caractères : ")
ancien_caractere = input("Entrez le caractère à remplacer : ")
nouveau_caractere = input("Entrez le nouveau caractère : ")
chaine_modifiee = remplacer_caractere(chaine, ancien_caractere, nouveau_caractere)
print("La chaîne modifiée est :", chaine_modifiee)
