from TP5_1 import Marienbad

if __name__ == "__main__":
    nom1=input("Joueur 1 entrer votre nom:  ")
    nom2=input("joueur 2 entrer votre nom:  ")
    print("\n")
    jeu=Marienbad(nom1,nom2)
    print("Joueur1 = {}".format(nom1))
    print("Joueur2 = {}\n".format(nom2))
    while( jeu.termine()==0) :
      print(jeu)
      print("--------------Prochain joeur : {} -------------\n".format(nom1))
      t=int(input("Dans quel tas voulez-vous retirer vos allumettes ?:  "))
      
      while (t>6 or t<1):
        print("Entrez un  numero de tas compris entre [1 , 6]")
        t=int(input("Dans quel tas voulez-vous retirer vos allumettes ?: \n"))
      if jeu.extra(t):
        while jeu.extra(t):
          print("Ce tas est vide\n") 
          t=int(input("Dans quel tas voulez-vous retirer vos allumettes ?: \n"))
          while t>6 or t<1:
            print("Entrez un  numero de tas entre 1 et 6")
            t=int(input("Dans quel tas voulez-vous retirer vos allumettes ?: \n"))
        
      n=int(input("Combien d'allumettes voulez-vous retirer  ?: \n"))
      if n>6 or n<1:
        while n>6 or n<1:
         print("le nombre d'allumettes est compris entre  [1 et le numero de la rangee]")
         n=int(input("Combien d'allumettes voulez-vous retirer vos allumettes ?:  \n"))
      

      while (not jeu.verifie(t,n)):
        
          print("Le nombre d'allumettes d'allumetes ne correspond pas\n")
          n=int(input("Combien d'allumettes voulez-vous retirer vos allumettes ?:  \n"))
          if n>6 or n<1:
           while n>6 or n<1:
             print("Entrez un nombre entre 1 et 6")
             n=int(input("Combien d'allumettes voulez-vous retirer vos allumettes ?: \n"))
      jeu.enlever(n,t)
    if jeu.tour%2==0 :
      print("Le gagnant est {}".format(nom1))


        
          