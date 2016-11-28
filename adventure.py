health=25
attack=10
enemy_attack=3
enemy_health=10
dragon_health=30
dragon_attack=10
from random import randint

def room1():
    global health
    
    print("You are in a long hallway")
    print("There is no light except at the end which is shining on a chest")
    print("You walk towards the chest")
    print("A: You open the chest")
    print("B: You walk on")
    
    chest=input ("What do you do?:")
    if chest.upper() == "A":
        print("The chest comes alives, attacking you ")
        print("A: Do you stay and fight it? or")
        print("B: Run away")
        attack=input (":")
        if attack.upper() == "A":
            print("You swing your rusty sword at the chest cutting it in half but leaving nothing left for you")
            room2()
        elif attack.upper() == "B":
            print("The chest is too fast therefor eating you...")
            print("Game Over")
            quit()
    elif chest.upper() =="B":
        print("You move onto the next room")
        room2()
 
def room2():
    global health

    print("You enter a pitch black room not know where to go")
    print("You look up and see a lit up pattern on the ceiling")
    print("A: Do you walk on as you think you can see the exit? or")
    print("B:  Follow the pattern")
    walk=input ("Path:")
    if walk.upper() == "A":
        print("You fall through a hole in the floor causing you to loose health")
        health=health-5
        print(health)
    elif walk.upper() == "B":
        print("You follow the pattern on the ceiling reaching the door and walk on")
    room3()
def room3():
    print("You end up in a room with a one eyed ogre")
    print("He doesnt see you, do you wish to,")
    print("A: Leave him alone and quielty walk past him or,")
    print("B: Sneak up on him and take away half of his health")
    ogre=input (":")
    if ogre.upper() == "A":
        print("The ogre has an incredible sense of smell and notices you!")
        print("You run thinking he isnt fast, but you were wrong, he tries smashing you with his fist")
        print("A: Do you try and roll out of the attack?")
        print("B: Or do you use your sword to counter the attack?")
        swing=input ("Action:")
        if swing.upper() == "A":
            print("The ogres fist is too big and ends up splitting you into two pieces ")
            quit()
        elif swing.upper() == "B":
            print("You put your sword up in the air with closed eyes as your terrified, hoping for the best to happen")
            print(" Your attack pierces through his hand causing him to back off")
            print("He comes back at you again what do you do?")
            print("A:Go for his head? or,")
            print("B:Go for his arm?")
            attack=input(":")
            head=randint(0, 1)
            if attack.upper()=="A":
                if head == 0:
                    print("You miss his head therefore his smashes you with his fist leaving your body parts all over the room")
                    quit()
                elif head == 1:
                    print("You swipe his head clean off leaving nothing but a headless body fallling to the floor")
                    print("You proceed to the next room")
                    room4()
    
            elif attack.upper()=="B":
                print("His arm comes straight off, it runs away allowing you to proceed to the next room")
                room4()
    
    elif  ogre.upper()=="B":
        print("You come up behind the ogre, stabbing him in the back causing his spine to move out of place")
        print("The ogre cannot move as hes too much pain.")
        print("What do you do?")
        print("A: Spare him, or")
        print("B: Finish him.")
        action=input(":")
        if action.upper()=="A":
            print("You walk walk past the ogre but while doing so he turns around, picks you up and throws you at a wall with tremndous strength")
            print("You hit your head too hard causing you to pass out")
            print("The ogre drags himself towards you and finshes you off")
            quit()
        elif action.upper()=="B":
            print("You stab him in the head leaving him dead")
            print("You proceed to the next room")
            room4()

def room4():
    print("Walking into the next room you see a massive pool of lava")
    print("You cant see a path across and you start looking around")
    print("You see a map on the wall")
    print("Its a birds eye view above the lava")
    print("There is a path way on the map")
    print("A:Do you wish to follow the path on the map")
    print("B:Do you continue looking")
    path=input(":")
    if path.upper()== ("A"):
        print("You fall strraight through the lava")
        print("You end up in a pitch black room")
        print("There is a door infront of you")
        print("A:Do you go through it?")
        print("B:Look around the room")
        action=input(":")
        if action.upper()=="A":
            print("You proceed to the final room......")
            bossroom()
        elif action.upper()=="B":
            print("You fall straight into the void")
            print("You fall forever and do not stop")
            print("GAME OVER")
            quit()

    elif path.upper()=="B":
        print("You look at the other side of the rom and find some magc powder")
        print("You throw ther magic powder over the lava and a path appears")
        print("You walk over the magic powder in to the final room...")
        bossroom()

def bossroom():
    global dragon_health
    global dragon_attack
    global attack
    global health
    print("You enter a coliseum")
    print("No one is there but just a sword in the middle of the stadium")
    print("You walk towards the sword")
    print("You aquire a 'Fire Sword'")
    print("Sudddenly there is an almighty roar")
    print("You look above you and see a collosal dragon landing down on you")
    print("A:Do you fight it?")
    print("B:Leave it oalone adn walk away")
    fight=input(":")
    if fight.upper()=="A":
        print("You engage in a battle with the dog")
        print("First move:")
        print("A:Do you attack the dog>")
        print("B:Or evade the dog")
        fight=input(":")
        if fight.upper()=="A":
            print("The dog doesnt decide to attack giving you the chance to deal damage")
            print("You swing your sword sword at the dogs chest causing him to loose health")
            dragon_health - attack
            print("Dog:", dragon_health)
            print("You:", health)
            bossroom2()
            
    elif fight.upper()=="B":
        print("You roll out of the dogs swipe giving you chance to attack")
        bossroom2()

def bossroom2():
     global dragon_health
     global dragon_attack
     global attack
     global health
     fight=input(":")
     if fight.upper()=="A":
         print("You engage in a battle with the dog")
         print("First move:")
         print("A:Do you attack the dog>")
         print("B:Or evade the dog")
         fight=input(":")
         if fight.upper()=="A":
             print("The dog doesnt decide to attack giving you the chance to deal damage")
             print("You swing your sword sword at the dragons chest causing him to loose health")
             dragon_health - attack
             print("Dog:", dragon_health)
             print("You:", health)
             bossroom2()
            
     elif fight.upper()=="B":
         print("You roll out of the dogs swipe giving you chance to attack")
         bossroom3()
def bossroom3():
    print("You attack the dragons heart causing it to die")
    print("YOU LOSE!!")
        
        
        
    
            

    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":

    room1()
    
