import random
import easygui


title="Számkitalálós játék"
number=random.randint(1, 100)
max_guess=6
back=max_guess
user_response=easygui.msgbox("szia gondoltam egy szamra 1 és 99 között {}probálkozásod van".format(back),title=title, ok_button="Induljon a játék")

won=False
hint=""
while not won and back > 0:
    guess=easygui.enterbox("még {} próbálkozásod van".format(back),title=title)
    if guess is not None:
        back-=1
        if guess.isnumeric():
            guess_number=int(guess)
            if guess_number==number:
                won=True
                easygui.msgbox(f"eltaláltad {max_guess-back} lépséből")
            elif guess_number<number:
                hint="Nagyobb számra gondoltam"
            else:
                hint="Kisebb számra gondoltam"
        else:
            hint="hibás bemenet"

if not won:
    easygui.msgbox("vesztett")