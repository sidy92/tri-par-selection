#Nous avons créer un programme Python pour trier les éléments d’un tableau à l’aide du tri par sélection. Dans l’algorithme de tri par sélection, tout d'abord nous cherchons l’élément le plus petit et on le met au bon endroit. Ensuite nous échangeons l’élément en cours avec le prochain élément le plus petit.

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le minimum
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]


print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])