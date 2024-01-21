file_name = "offres_transport.txt" 
file_na = "reservation.txt"  
class Date:
    def __init__(self, jour, mois, année):
        self.jour = jour
        self.mois = mois
        self.année = année


class Offre:
    def __init__(self, Ref_Offre, ville_depart, ville_arrivee, disponible):
        self.Ref_Offre = Ref_Offre
        self.ville_depart = ville_depart
        self.ville_arrivee = ville_arrivee 
              
    
class OffreTransportAllerSimple(Offre):
    def __init__(self, Ref_Offre, ville_depart, ville_arrivee, date, prix):
        super().__init__(Ref_Offre, ville_depart, ville_arrivee)
        self.date = date
        self.prix = prix
    
    def sauvegarder(self):
        f = open(file_name, "a")
        f.write(f"{self.Ref_Offre},'AS' ,{self.ville_depart},{self.ville_arrivee},{self.date},{self.prix},\n")
 
class resevation(Offre): 
    def __init__(self,Ref_réservation,Type_Offre,Ref_Offre, ville_depart, ville_arrivee,Date_départ,Date_retour,genre,nom,prenom,pays_passeport,n_passeport,etat_reservation,total_a_payer):
        super().__init__(Ref_Offre, ville_depart, ville_arrivee)
        self.Ref_réservation = Ref_réservation
        self.Type_Offre = Type_Offre
        self.Date_départ = Date_départ
        self.Date_retour = Date_retour
        self.genre = genre
        self.nom = nom
        self.prenom = prenom
        self.pays_passeport = pays_passeport
        self.n_passeport = n_passeport
        self.etat_reservation = etat_reservation
        self.total_a_payer = total_a_payer

    def sauvegarder(self):
        f = open(file_na, "a")
        f.write(f"{self.Ref_réservation} ,{self.Type_Offre},{self.Date_départ},{self.Date_retour},{self.genre},{self.nom},{self.prenom},{self.pays_passeport},{self.n_passeport},{self.etat_reservation},{self.total_a_payer},\n")
 
    

class OffreTransportAllerRetour(Offre):
    def __init__(self, Ref_Offre, ville_depart, ville_arrivee, date_depart, date_arrivee, prix):
        super().__init__(Ref_Offre, ville_depart, ville_arrivee)
        self.date_depart = date_depart
        self.date_arrivee = date_arrivee
        self.prix = prix
    def sauvegarder(self):
        f = open(file_name, "a")
        f.write(f"{self.Ref_Offre}, 'AR' ,{self.ville_depart},{self.ville_arrivee},{self.date_depart},{self.date_arrivee},{self.prix},\n")
 

class OffreFormuleComplete(Offre):
    def __init__(self, Ref_Offre, ville_depart, ville_arrivee, date_depart, date_arrivee, type_offre, prix):
        super().__init__(Ref_Offre, ville_depart, ville_arrivee)
        self.date_depart = date_depart
        self.date_arrivee = date_arrivee
        self.type_offre = type_offre
        self.prix = prix
    def sauvegarder(self):
        f = open(file_name, "a")
        f.write(f"{self.Ref_Offre}, 'FC' ,{self.ville_depart},{self.ville_arrivee},{self.date_depart},{self.date_arrivee},{self.type_offre},{self.prix},\n")
 

class Hébergement(Offre):
    def __init__(self,Ref_Offre, ville_depart, ville_arrivee ,date_debut, nb_nuits, type_hebergement, prix_par_nuit):
        super().__init__(Ref_Offre, ville_depart, ville_arrivee)
        self.date_debut = date_debut
        self.nb_nuits = nb_nuits
        self.type_hebergement = type_hebergement
        self.prix_par_nuit = prix_par_nuit
    
    def sauvegarder(self):
        f = open(file_name, "a")
        f.write(f"{self.Ref_Offre},'HB',{self.ville_depart},{self.ville_arrivee},{self.date_debut},{self.nb_nuits},{self.type_hebergement},{self.prix_par_nuit},\n")

    
    
def Liste_Cmd():
    return(["0. Déclarer une offre",
       "1. Mettre à jour une offre (changer la date ou/et le prix) ",
       "2. afficher offre",
       "3. Bloquer une offre (rendre obsolète une offre au lieu de la supprimer du fichier" ,
       "4. Faire une réservation",
       "5. Confirmer ou annuler une réservation ",
       "6. nombre de réservation total",
       "7. nombre de réservations par type ", 
       "8. nombre total des offres",
       "9. nombre de réservation selon le type ",
       "10. le total du chiffre d'affaire ",
       "13. quitter",      
       ])
def Menu(M):
    for i in range(len(M)):
        print(M[i],'\n')
    return(input("Veuillez choisir un nombre entre 0 et " + str(len(M)-1)+" : "))
def saisir_offre (): 
    type = int(input("entrer 1 si vous voulez  transportsimple , 2 pour allerRetour , 3 pour formuleComplète") )         
    print("type",type)
    if type == 1 : 
        print("veuillez entrer une offre ")
        Ref_offre = input("veuillez saisir la référence de l'offre ")
        ville_depart= input("veuillez saisir la ville de départ ")
        ville_arrivee= input("veuillez entrer la ville d'arrivée ")
        date = input("entrer la date de départ : ")
        prix = input("entrer le prix")
        obj = OffreTransportAllerSimple(Ref_offre,ville_depart,ville_arrivee,date,prix)
        return obj

    elif type == 2 : 
        print("veuillez entrer une offre  ")
        Ref_offre = input("veuillez saisir la référence de l'offre ")
        ville_depart= input("veuillez saisir la ville de départ ")
        ville_arrivee= input("veuillez entrer la ville d'arrivée ")
        date_depart = input("entrer la date de départ : ")
        date_arrivee = input("entrer la date d'arrivée : ")
        prix = int(input("entrer le prix"))
        obj = OffreTransportAllerRetour(Ref_offre,ville_depart,ville_arrivee,date_depart, date_arrivee, prix)
        return obj
    
    elif type == 3 : 
        print("veuillez entrer une offre  ")
        Ref_offre = input("veuillez saisir la référence de l'offre ")
        ville_depart= input("veuillez saisir la ville de départ ")
        ville_arrivee= input("veuillez entrer la ville d'arrivée ")
        date_depart = input("entrer la date de départ : ")
        date_arrivee = input("entrer la date d'arrivée : ")
        type_offre = input("entrer soit semaine ou week-end : ")
        prix = int(input("entrer le prix"))
        obj = OffreFormuleComplete(Ref_offre,ville_depart,ville_arrivee,date_depart, date_arrivee, type_offre,prix)
        return obj
    
    else : 
        return "error"

def modifier_offre():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if ref == t[0]:
          new_price = int(input("Enter the new price: "))
          new_date_depart = input("Enter the new date depart: ") 
          t[4] = new_price
          t[5] = new_date_depart
          lines[i]  = ','.join([str(elem) for elem in t])
          with open(file_name, 'w', encoding='utf-8') as file: 
            file.writelines(lines) 
def modifier_offreAllerSimple():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if ref == t[0]:
          new_price = int(input("Enter the new price: "))
          new_date_depart = input("Enter the new date depart: ") 
          t[4] = new_price
          t[5] = new_date_depart
          lines[i]  = ','.join([str(elem) for elem in t])
          with open(file_name, 'w', encoding='utf-8') as file: 
            file.writelines(lines)

def modifier_offreAllerRetour():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if ref == t[0]:
          new_price = int(input("Enter the new price: "))
          new_date_depart = input("Enter the new date depart: ") 
          t[4] = new_price
          t[5] = new_date_depart
          lines[i]  = ','.join([str(elem) for elem in t])
          with open(file_name, 'w', encoding='utf-8') as file: 
            file.writelines(lines)

def modifier_offreFormuleComplete():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if ref == t[0]:
          new_price = int(input("Enter the new price: "))
          new_date_depart = input("Enter the new date depart: ") 
          t[4] = new_price
          t[5] = new_date_depart
          lines[i]  = ','.join([str(elem) for elem in t])
          with open(file_name, 'w', encoding='utf-8') as file: 
            file.writelines(lines)

def afficher_offre():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      for line in lines:
        print(line)
        t = line.split(",")
        if ref == t[0]:
          print('reference :',t[0])
          print('ville_depart :',t[2])
          print('ville_arrivéé :',t[3])

def afficher_offreAllerSimple():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      for line in lines:
        print(line)
        t = line.split(",")
        if ref == t[0]:
          print('reference :',t[0])
          print('ville_depart :',t[2])
          print('ville_arrivéé :',t[3])
          print('date du départ est :  ' , t[4])
          print("le prix est: " , t[5])

def afficher_offreAllerRetour():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      for line in lines:
        print(line)
        t = line.split(",")
        if ref == t[0]:
          print('reference :',t[0])
          print('ville_depart :',t[2])
          print('ville_arrivéé :',t[3])
          print('date du départ est :  ' , t[4])
          print("date d'arrivée est :  " , t[5])
          print("le prix est: " , t[6])

def afficher_offreFOrmuleCOmplete():
    ref = input("entrer la référence de l'offre")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      for line in lines:
        print(line)
        t = line.split(",")
        if ref == t[0]:
          print('reference :',t[0])
          print('ville_depart :',t[2])
          print('ville_arrivéé :',t[3])
          print('date du départ est :  ' , t[4])
          print("date d'arrivée est :  " , t[5])
          print("le type de l'offre est :" , t[6])
          print("le prix est: " , t[7])

def bloquer_offre():
   ref = input("entrer la référence de l'offre que vous souhaiter bloquer : ")
   with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        print(line)
        t = line.split(",")
        if ref == t[0]:
            t[0] = "absolète"
            lines[i]  = ','.join([str(elem) for elem in t])
            print(lines[i])
            with open(file_name, 'w', encoding='utf-8') as file: 
                file.writelines(lines)

def faire_réservation():
    print("vous allez faire une réservation : ")
    Ref_réservation = input("entrer la référence de la réservation : ")
    Type_Offre = input("entrer le type de l'offre : ")
    Date_départ = input("entrer la date du départ correctement : ")
    Date_retour = input ("entrer la date d'arrivée correctement : ")
    genre = input("entrer F pour femme et H pour homme : ")
    nom = input("entrer votre nom : ")
    prenom = input("entrer votre prenom : ")
    pays_passeport =input("entrer votre nationalité : ")
    n_passeport =int(input("entrer le numéro du passeport : "))
    etat_reservation = input("entrer soit en cours, soit annulée, soit confirmée : ")

def afficher_réservation():
    ref = input("entrer la référence de la réservation : ")
    with open(file_na, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      for line in lines:
        print(line)
        t = line.split(",")
        if ref == t[0]:
          print('reference de la réservation :',t[0])
          print("type de l'offre :",t[1])
          print('date_départ :',t[2])
          print('genre du réservateur:',t[3])
          print("nom du réservateur :",t[4])
          print('prenom du réservateur :',t[5])
          print('pays du passeport :',t[6])
          print('numero du passeport:',t[7])
          print("état de la réservation :",t[4])

def confirmation () : 
    ref = input("entrer la référence de la réservation")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if ref == t[0]:
          confirmer = input("irez vous confirmer ou annuler la réservation ?") 
          if confirmer == "annuler" or confirmer == "confirmer" : 
            t[9] = confirmer
            lines[i]  = ','.join([str(elem) for elem in t])
            with open(file_name, 'w', encoding='utf-8') as file: 
                file.writelines(lines)
          else : 
            print("veuiller saisir l'état de votre réservation")

def nmb_offre_type():
    nbr=0
    types= input("entrer le type de l'offre, sous forme de AS ou AR ou FC ou HB : ")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if type == t[1]:
           nbr=nbr+1

def total_offre():
    types= input("entrer le type de l'offre, sous forme de AS ou AR ou FC ou HB : ")
    with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",") 
      nbr=len(t)

def date_précise():
   date_depart=input("entrer la date du départ : ")
   date_arrivee=input("entrer la date d'arrivée : ")
   with open(file_name, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if t[1] == 'AS' and t[4]==date_depart:
           nbr1 = nbr1 + 1
        elif t[1] == 'AS' and t[4]==date_depart and t[5]==date_arrivee:
           nbr2 = nbr2+1
        elif t[1] == 'AS' and t[4]==date_depart and t[5]==date_arrivee:
           nbr3 = nbr3+1
        else : 
           nbr=0
      nbr=nbr1+nbr2+nbr3
      print("le nombre total des offres est: " , nbr)

def nbr_reservation():
   type = input("entrer soit annuler soit confirmé soit global : ")
   with open(file_na, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
        if t[9] == "annuler" : 
           nbr1 = nbr1+1
           print("le nombre de réservation annuler est : " , nbr1)
        elif t[9] == "confirmer" : 
           nbr2 = nbr2+1
           print("le nombre de réservation annuler est : " , nbr2) 
        print ("le nombre total des résevation est : " , nbr1+nbr2)

def nbr_reservation1() : 
   ville_arrivee = input("entrer votre destination : ")
   date_départ = input("entrer la date du départ : ")
   date_arrivee = input("entrer la date arrivee : ")
   n_passeport = int(input("entrer le numéro du passeport : "))
   nationalité = input("entrer la nationalité : ")
   with open(file_na, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
      if t[2] == ville_arrivee : 
        nbr = nbr + 1
        print("le nombre de réservation d'après la ville d'arrivéé que vous avez séléctionnez est : " , nbr)
      elif t[5] == date_départ and t[6] == date_arrivee : 
        nbr1 = nbr1+1
        print("le nombre de résevations d'après la date d'arrivée et la date du départ que vous avez séléctionne est :" , nbr1)
      elif t[11] == n_passeport : 
        nbr3 = nbr3+1
        print("le nolbre de réservations d'après votre identité est : " , nbr3)
      elif t[10] == nationalité : 
        nbr4=nbr4+1
        print("le nombre de réservations d'après votre nationalité est : " , nbr4)

def chiffre_affaire_tot():
    with open(file_na, 'r', encoding='utf-8') as file: 
      lines = file.readlines() 
      i = -1
      for line in lines:
        i = i +1
        t = line.split(",")
    prix = t[-1]*len(t)
    print("le prix global est : " , prix)
    
def principal():
    while True:
        print('\n','\n')
        choix=Menu(Liste_Cmd())
        if choix=='0':
           offre = saisir_offre()
           offre.sauvegarder()
        elif choix=='1':
           offre = modifier_offre()
           offre.sauvegarder()          
        elif choix=='2':
           offre = afficher_offre()        
        elif choix=='3':
            offre = bloquer_offre() 
            offre.sauvegarder()            
        elif choix=='4':
            offre = faire_réservation()  
            offre.sauvegarder()            
        elif choix=='5':
            offre = confirmation()   
            offre.sauvegarder           
        elif choix=='6':
            offre = nbr_reservation()              
        elif choix=='7':
            offre = nmb_offre_type()             
        elif choix=='8':
            offre = total_offre()             
        elif choix=='9':
            offre = nbr_reservation1()              
        elif choix=='10':
            offre = chiffre_affaire_tot()                    
        elif choix=='13':
            print("AU REVOIR")
            break           
        else:
            print("Erreur : ",'\n'," recommencez svp et veuillez saisir un nombre entre 0 et 13 : ",'\n')
principal()
