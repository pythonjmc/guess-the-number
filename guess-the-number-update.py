import random

INVITE = "Suggest a number"

QUITTER = -1
QUIT_TXT = 'q'
QUIT_MSG = "Thanks for playing!"
QUIT_CONFIRMER = "Are you sure to leave the game ? (O/n) ?"

def confirmer_quitter():
    confi = input(QUIT_CONFIRMER)
    if confi == 'n':
        return False
    else:
        return True

def jouer_tour():
    nbr_secret = random.randint(1,100)
    nbr_saisies = 0
    while True:
        nbr_joueur = input(INVITE)
        if nbr_joueur == QUIT_TXT:
            if confirmer_quitter():
                return QUITTER
            else:
                continue
        nbr_saisies = nbr_saisies + 1
        if nbr_secret == int(nbr_joueur):
            print("Correct")
            return nbr_saisies
        elif nbr_secret > int(nbr_joueur):
            print("To small")
        else:
            print("To big")

total_tours = 0
total_saisies = 0
msg_stat = 0

while True:
    total_tours = total_tours + 1
    print("We go around " + str(total_tours))
    print("forward to the guesswork!")

    ce_tour = jouer_tour()

    if ce_tour == QUITTER:
        total_tours = total_tours - 1
        if total_tours == 0:
            msg_stat = "First round not finish ! " + "Would you restart ?"
        else:
            moy = str(total_saisies / float(total_tours))
            msg_stat = "You did " + str(total_tours) + "round(s). Average of" + str(moy)

    total_saisies = total_saisies + ce_tour
    print("TYou did " + str(ce_tour) + "entries.")
    moy = str(total_saisies / float(total_tours))
    print("Your average number of entries/round= " + moy)
    print("")

print(QUIT_MSG)
print(msg_stat)
