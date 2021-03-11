from random import randint
def report(stamina):
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina > 1:       
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
def alian(): 
    stamina=10
    while stamina>0:
        user=input("which way to you choice Enter a move. \n1.Hit \n2.attack \n3.fight \n4.run \n-:")
        if user=="fight":
            print("Fight how? You have no weapons, silly space traveler!")
        elif user=="hit" or user=="attack":
            a=randint(0,stamina)
            print(a)
            stamina=stamina-a
            report(stamina)
        elif user=="run":
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
alian()