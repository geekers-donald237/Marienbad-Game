print("\t\t*******************Jeu Des Allumettes*****************\n")

class Marienbad:
    allu=[1,2,3,4,5,6]
    tas=(1,2,3,4,5,6)
    tour = 0

    #print("tas  :{}".format(tas))
    def __init__(self,j1="joueur1",j2="joueur2"):
        self.j1=j1
        self.j2=j2
    
    def __str__(self):
        return ("tas\t  :  {} \nallumetes :  {}".format(self.tas,self.allu))
    
    def verifie(self,t,n):
        if self.allu[t-1] >= n : 
            return 1
        else:
            return 0  
    
    def enlever(self,n,t):
        self.allu[t-1] = self.allu[t-1] - n
        self.tour += 1
        if self.tour%2==0:
            print("-------Prochain joueur : {}--------\n".format(self.j1))
        else:
            if self.tour%2!=0:  
                print("-------Prochain joueur : {}--------\n".format(self.j2))      
    
    def termine(self):
        if self.allu[0]==0 and self.allu[1]==0 and self.allu[2]==0 and self.allu[3]==0 and self.allu[4]==0 and self.allu[5]==0:
            return 1
        else:
            return 0          

    def extra(self,t):
        if self.allu[t-1]==0:
            return 1
        else:
            return 0    


              
