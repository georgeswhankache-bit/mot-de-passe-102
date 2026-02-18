from tkinter import *
from tkinter.messagebox import *

#premiere verification
def verifnombre(x):
    """fonction qui vérifie que le mdp a plus que 8 character.
    entré : le mot de passe
    sorti : bouléin si le mot de passe et bon ou pas
    """
    assert(type(x)==str), "Le mot de passe doit etre une chaine de caractère" #precondition
    return len(x) >= 8

#deuxieme verif
def verifMaj(x):
    """fonction qui vérifie que le mdp a au moins 1 character majuscule.
    entré : le mot de passe
    sorti : si le mot de passe est bon ou pas
    """
    assert(type(x)==str), "Le mot de passe doit etre une chaine de caractère" #precondition
    return any(i.isupper() for i in x) # verifie la presence d'une lettre majuscule (upper)

#troisième verif
def verifMin(x):
    """fonction qui vérifie que le mdp a au moins 1 character minuscule.
    entré : le mot de passe.     
    sorti : si le mot de passe est bon ou pas.
    """
    assert(type(x)==str), "Le mot de passe doit etre une chaine de caractère" #precondition
    return any(i.islower() for i in x) # verifie la presence d'une lettre minuscule (lower)

#quatrième verif
def verifChi(x):
    """Verifie si le mdp contient un chiffre"""
    return any(i in "0123456789" for i in x)

#cinquième verif
def verifCar(x):
    """Verifie si le mdp contient un caractere special"""
    return any(i not in "0123456789AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn" for i in x)

#lance une verification de mot de passe
def verifConfirm(mdp1, mdp2):
    """verififie la corespondance entre le mdp1 et le 2
    sorti : si le mot de passe corespond ou pas.
    """
    assert(type(mdp1)==str), "Le mot de passe doit etre une chaine de caractère" #precondition
    assert(type(mdp2)==str), "Le mot de passe doit etre une chaine de caractère" #precondition
    return mdp1 == mdp2 and mdp1 != ""
    

def set_led(widget, state):
    """fonction qui creer un voyant changant de couleur entre rouge et vert"""
    if state:
        widget.config(bg="green")
    else:
        widget.config(bg="red")

def mdp(x,y):
    """fonction qui lance la vérification d'un mot de passe
    entré : le mot de passe
    
    elle test a la fin si tout corespond et le fait apparaitre si c'est bon.
    """
    Vn=verifnombre(x) #appele de la premiere verif
    Vmaj=verifMaj(x)#appele la deuxieme verif
    Vmin=verifMin(x)#appele la troisième verif
    same = verifConfirm(x, y)
    Vchi = verifChi(x)#appelle la quatrième verif
    Vcar = verifCar(x)#appelle la cinquième verif
    print(Vn, Vmaj, Vmin, Vchi, Vcar)
        
    #set les voyant colorer
    set_led(led_longueur, Vn)
    set_led(led_maj, Vmaj)
    set_led(led_min, Vmin)
    set_led(led_chi, Vchi)
    set_led(led_car, Vcar)

        
    if Vn and Vmaj and Vmin and same and Vchi and Vcar:
        message_label.config(text="Mot de passe valide ✔", fg="green")
        Mafenetre.after(1200, Mafenetre.destroy)  # ferme après 1.2s
    else:
        message_label.config(text="Mot de passe invalide ❌", fg="red")
        if same:
            message_label.config(
            text="Les mots de passe correspondent ✔",
            fg="green"
            )
        else:
            message_label.config(
            text="Les mots de passe ne correspondent pas ❌",
            fg="red"
            )

# Nouvelle fonction pour update en temps réel
"""Prendre en compte tout type d'arguments. Récupère ce que l'utilisateur rentre
dans les champs de textes. Permet de mettre a jour en temps reel la validité du mdp"""
def mdp_live(*args):
    mdp(Motdepasse.get(), MotdepasseC.get())

# Création de la fenêtre principale (main window)
Mafenetre = Tk() #creation de la fenetre
Mafenetre.geometry("500x360") #taille de la fenetre
Mafenetre.title("Entrer en enfer") #titre de la fenetre
Mafenetre.resizable(False, False) #enleve la posibiliter de modifier la taille de la fenetre

#Titre
message_label = Label(Mafenetre, text="Pour rentrer en Enfer, \nveuillez creer un mot de passe : ", font=("Arial", 13, "bold"),bg="darkred")
message_label.grid(row=0, column=1, columnspan=3, pady=10)


#label "mot de passe"
Label1 = Label(Mafenetre, text = 'Mot de passe : ',bg="darkred", font=("Arial",14,"bold"))
Label1.grid(row=1, column=0, padx=5, pady=5)

# Champ de texte
Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, show='*', bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.grid(row=1, column=1, padx=5, pady=5)

#Label "Confirmation"
Label1 = Label(Mafenetre, text = 'Confirmez : ', bg="darkred", font=("Arial",14,"bold"))
Label1.grid(row=7, column=0, padx=5, pady=5)

# Champ de texte
MotdepasseC= StringVar()
Champ2 = Entry(Mafenetre, textvariable= MotdepasseC, show='*', bg ='bisque', fg='maroon')
Champ2.focus_set()
Champ2.grid(row=7, column=1, padx=5, pady=5)

# Boutton valider
Bouton = Button(Mafenetre, text='Valider votre entrer au enfer',bg="red", font=("bold"),command=lambda: mdp(Motdepasse.get(),MotdepasseC.get()))
Bouton.grid(row=10, column=1, padx=5, pady=5)

# Voyants
Label(Mafenetre, text="Longueur ≥ 8").grid(row=2, column=0)
led_longueur = Label(Mafenetre, width=1, bg="red")
led_longueur.grid(row=2, column=1)

Label(Mafenetre, text="Majuscule").grid(row=3, column=0)
led_maj = Label(Mafenetre, width=1, bg="red")
led_maj.grid(row=3, column=1)

Label(Mafenetre, text="Minuscule").grid(row=4, column=0)
led_min = Label(Mafenetre, width=1, bg="red")
led_min.grid(row=4, column=1)

Label(Mafenetre, text="Chiffre").grid(row=5, column=0)
led_chi = Label(Mafenetre, width=1, bg="red")
led_chi.grid(row=5, column=1)

Label(Mafenetre, text="Caractère Spécial").grid(row=6, column=0)
led_car = Label(Mafenetre, width=1, bg="red")
led_car.grid(row=6, column=1)

#text qui s'affiche quand on a une erreur
message_label = Label(Mafenetre, text="", font=("Arial", 15, "bold"),bg="darkred")
message_label.grid(row=9, column=0, columnspan=3, pady=10)

"""
# Compte le nombre de vérifications égales à True
def scor(x):    
    results = [verifnombre(x), verifMaj(x), verifMin(x), verifChi(x), verifCar(x)]
    return sum(results)

message_label3 = Label(Mafenetre, font=("Arial", 13, "bold"))
message_label3.grid(row=8, column=0, columnspan=3, pady=10)

def afficher_score():
    x = entry.get()  # On récupère le mot de passe
    score = scor(x)
    score2 = score / 5 * 100

    if score < 100:
        message_label3.config(text=f"Le score de complexité est {score2:}% (essayez encore !😈)", bg="darkred")
        message_label3.grid(row=8, column=0, columnspan=3, pady=10)
    else:
        message_label3.config(text=f"Le score de complexité est de 100% (vous êtes fort !💪)", bg="darkred")
        message_label3.grid(row=8, column=0, columnspan=3, pady=10)
"""

# Bouton pour montrer/masquer le mot de passe principal
mdp_visible = False
def montrermdp():
    global mdp_visible
    mdp_visible = not mdp_visible
    Champ.config(show='' if mdp_visible else '*')

Button(Mafenetre, text='👁', command=montrermdp).grid(row=1, column=2, padx=5, pady=5)

# Bouton pour montrer/masquer le mot de passe de confirmation
confirmation_visible = False
def montrerconfirmation():
    global confirmation_visible
    confirmation_visible = not confirmation_visible
    Champ2.config(show='' if confirmation_visible else '*')

Button(Mafenetre, text='👁', command=montrerconfirmation).grid(row=7, column=2, padx=5, pady=5)

#background color
Mafenetre.configure(bg="darkred")

#Trace pour la mise à jour en direct
"""Permet de savoir quand est-ce que le champ de texte
est modifié."""
Motdepasse.trace_add("write", mdp_live)
MotdepasseC.trace_add("write", mdp_live)
    
#lanceur de la fenetre
Mafenetre.mainloop()