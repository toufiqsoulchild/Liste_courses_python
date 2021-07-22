def liste():
    a = "1: Ajouter un élément à la liste"
    b = "2: Retirer un élément de la liste"
    c = "3: Afficher la liste"
    d = "4: Vider la liste"
    e = "5: Quitter\n"
    f = 0
    courses = []
    options = [a, b, c, d, e]
    while f != 5:
        for choix in options:
            print(choix)
        
        f = int(input("Faite votre choix: "))
        if f == 1:
            courses.extend([input("Que voulez ajouter ? ")])
        elif f == 2:
            stuff = (input("Que voulez retirer ? "))
            if stuff in courses:
                courses.pop(courses.index(stuff))
                print(f"\nl'élément {stuff} à bien été supprimée de la liste.\n")
            else: 
               print(f"\nL'élément {stuff} n'est pas dans la liste.\n")
        elif f == 3:
            if len(courses) == 0:
                print("\nLa liste ne contient aucun élément\n")
            else:  
                print("\nVoici le contenu de la liste: ")
                for stuff in courses:
                    print(f" {courses.index(stuff)+1}. {stuff}\n")
        elif f == 4:
            for stuff in courses:
                courses.remove(stuff)
            print("\nLa liste a été vidée de sont contenu.\n")
               
    print("\nA bientôt\n")
liste()
