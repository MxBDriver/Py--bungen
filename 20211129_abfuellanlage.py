schalterEIN = 0
schalterAUS = 0
motor = 0
befuellung = False
lichtSchranke1 = False
lichtSchranke2 = False
schalterNOTAUS = False
keineFlaschenCount = 0
falseCount = 0
anlagenfuehrer = "Bitte überprüfen Sie die Flaschenzufuhr"
mechaniker = "Bitte unterstützen Sie den Anlagenführer"

#Anlage Einschalten nur bei nicht aktivierten Notaus
abfrageNOTAUS = bool(input("Ist der Notaus Schalter betätigt? 'Boolean Abfrage' \n"))
while schalterNOTAUS == False:
    abfrageEIN = int(input("SchalterEIN eingeschaltet? 'AN=1/AUS=0' \n"))
    abfrageAUS = int(input("SchalterAUS eingeschaltet? 'AN=1/AUS=0' \n"))
    while schalterEIN == 1 and schalterAUS == 0:
        motor = 1
        
        #Flaschen Ausfahlmeldung
        if lichtSchranke1 == False:
            keineFlaschenCount += 1
            print(keineFlaschenCount + " fehlende Flaschen")
            if keineFlaschenCount == 3:
                print("Nachricht an den Anlagenführer: \n" + anlagenfuehrer)
                falseCount += 1
                keineFlaschenCount = 0
            elif falseCount == 3:
                print("Nachricht an den Mechaniker: \n" + mechaniker)
                keineFlaschenCount = 0
                falseCount = 0
                schalterNOTAUS == 1
        else:
            print("Alles in Ordnung")
            
        #Befüllung
        if lichtSchranke1 == True:
            motor = 0
            befuellung = True
            for i in range(1,11):
                print(i + " Sekunden, Befüllung läuft!")
            else:
                befuellung = False    
        else:
            motor = 1
            
    #Schalter AUS aktiv und anlage hernuterfahren
    else:
        if schalterAUS == 1:
            motor = 0
            schalterEIN = 0
            if befuellung == True:
                for i in range(1,11):
                    print(i + " Sekunden, Befüllung läuft!")
            else:
                befuellung = False
                break
                
#NOTAUS ausgelöst, sofortiger Anlagen stillstand                
else:
    while schalterNOTAUS == True:
        motor = 0
        befuellung = False
        print("Notaus betätigt!")
        schalterNOTAUS = bool(input("Notaus Schalter noch betätigt? 'Boolean Abfrage' "))
    else:
        schalterAUS = 1
        
            