import csv 
descripteur = ('sexe','preusuel','annais','nombre')

#fonction lecture retourne LD des données 
def lecture (nom_fichier , delimiter = ';' , encoding = 'utf-8') :
    with open (nom_fichier , newline='' , encoding = encoding) as f : 
        lectures = csv.DictReader(f , delimiter = delimiter)
        table_prenom = list(lectures)   
    return table_prenom


#fonction compte retourne le nombre de prenom en une année
def compte (prenom , annees) : 
    c=0
    for ligne in table_Prenom : 
        if ligne['preusuel'].lower() == prenom.lower() and ligne['annais'] == annees : 
            c+=int(ligne['nombre'])
    return c 
            
#fonction liste des prénoms féminins donnés en 2000
def prenom_feminin (): 
    prenom_2000 = []
    for ligne in table_Prenom : 
        if ligne['sexe'] == '2' and ligne['annais']=='2000' and ligne['preusuel'] !='_PRENOMS_RARES' : 
            prenom_2000.append((ligne['preusuel'], int(ligne['nombre'])))
            #trie en fonction du nombre a l'ordre decroisant 
    prenoms_tries = sorted(prenom_2000, key=lambda e: e[1], reverse=True)  
    return prenoms_tries      

#fonction prenom rare faible 
def prenom_rare_faible () :
    faible = 1250
    annee  = 1900
    for ligne in table_Prenom : 
        if ligne['preusuel'] == '_PRENOMS_RARES' and int(ligne['nombre']) < faible:
            faible = int(ligne['nombre']) 
            annee  = ligne['annais']
    return annee

#fonction recurence de marie 
def compte_marie () :
    compteur = 0 
    for ligne in table_Prenom : 
        if ligne["preusuel"].lower() == 'marie' : 
            compteur += int(ligne['nombre'])
    return compteur
            
            
    
table_Prenom = lecture("nat2020.csv")
print("------------------bonjours!, nous allons commancer l'analyse des données!----------------\n")
print('la taille du fichier est : ',len(table_Prenom),'\n') 
print('------------------rechercher le nombre de prenom en une années precise-------------------\n')
prenom = input('veuillez entrer le prenom : ')
annees = input('veuillez entrer l''année : ')
print('le prenom donner apparait ',compte(prenom, annees),' fois \n')
print("------------------Extraire la liste des prénoms féminins donnés en 2000------------------\n")
prenoms_filles = prenom_feminin()
print('le prénom féminin le plus donné est : ',prenoms_filles[0],'\n')
print('------------------les prenoms rares------------------------------------------------------\n')
print('l''année ou les prenom rare on etait le plus faible est : ',prenom_rare_faible (),'\n')
print("------------------le champion est Marie!-------------------------------------------------\n")
print('le prenom marie reviens ',compte_marie (),'fois !\n')
print('------------------programme terminer, a trés bien tot!-----------------------------------')  