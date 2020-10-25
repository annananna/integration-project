# Ana Goglin
# I'm gonna try to make a game or something?
import random
name = input("What's your name? ")
print("Hi", name,"this is a super generic text based fighty adventure game with little fighty and no adventure :)")
# asking their name and saying hi
job = input("What job would you like to have? spell, sword, or stealth? \n (these will have not a lot of actual impact lol idk how to code that :p\n")
# assigning variables
exp = 0
lvl = 1
attack = 0
hp = 0
hp = lvl * 10
# exp=int(input(""))
# ^not a comment just saving this
lvl = lvl + (exp // 10)
print("Your level is:", lvl)
# using operators to use exp to determine level
print(
    "You're in a castle, or dungeon or something atmospherically fantasy game like that")
input("")
# setting up an enemy or something, using its number to make its health, v simple

def fight(action, enemy_hp): # made all the actions into functions so its easier
    print("You chose to fight :0")
    if action == "sword":
        print("Hey good thing you're a sword, you do better at fight")  # if and else inside an if else :0
        attack = (lvl * 3)
    else:
        attack = lvl * 2
    print("Wow you did", attack, "damage!")
    damage = enemy_hp - attack
    print("The Enemy now has", damage, "Health left\n")
    enemy_hp = damage
    return(enemy_hp)

def trivia(job):
    print("There's only one questions and no multiple choice, goodluck :) ")
    correct_answer = "twitter"
    # want to make more questions eventually (for next sprint thing tho)
    #make an array for multiple question options, and a random number or smth
    if job == "spell":
        print("The first letter is:", correct_answer[0])
    else:
        input("")
    answer = input("What was Twitter's original name? ") #make function for more answers/questions
    if answer.lower() == correct_answer:
        print("The dude is shooketh and cries in defeat, you win")
        enemy_hp = 0
        return(True)
    else:
        print("They laugh at you and you die, RIP", name)
        die = 1
        return(False)

def sneak(job):
    if job == "stealth":
        print("you try to sneak past, theres a 50% chance")
        chance = random.randint(0, 2)
    else:
        print("you try to sneak past, theres a 25% chance")
        chance = random.randint(0, 4)
    input("")
    if chance == 1:
        print("You've a snucked right past them :O")
        return(True) #snuck past
    else:
        print("couldn't get away")
        return(False)

def monster(hp,enemy_hp):
    action = (input( "Your actions are: fight, beat them at a trivia question, or sneak past them. \n What would you like to do? "))
    while (enemy_hp > 0):
        # trying to do a while loop if input isnt one the the expected reponses
        while (action != "fight") and (action != "trivia") and (
                action != "sneak") and (action != "run"):
            print("Check your spelling")
            action = str(
                input("What would you like to do? fight, trivia, or sneak "))
        if action == ("fight"):
            enemy_hp= fight(job, enemy_hp)
            if enemy_hp == 0:
                print("\n\nCongratulations on defeating enemy1")
                break
        elif action == ("trivia"):
            if trivia(job): #uses the true or false if snuck through to show the combat result
                break
            else:
                hp=0
                break

        elif action == ("sneak"):
            if sneak(job):
                print("You've a snucked right past them :O")
                break
        else:
            print("cant run away from a trainer battle")

        print("they attacks, deals ", enemy_num, "damage")
        print("You have", hp - enemy_num, "health left")
        hp -= enemy_num
        if hp <= 0:
            return(hp)
        else:
            print("What next?")
            action = (input(""))
    return(hp)

# while loop to keep in 'action zone' until the enemy is defeated
enemy_num = 1
for x in range(0,3):
    print("Omg! out of nowhere an convieniently also low level animal or monster appears!\n")
    print("This is enemy number", enemy_num,"out of however many I decide to add")
    enemy_hp = (enemy_num + 2) * 2
    input("")
    hp = monster(hp, enemy_hp)
    if hp == 0:
        print("You are dead")
        dead = 0
        break
    else:
        exp = exp + enemy_num * 7
        lvl = lvl + (exp // (lvl * 10))

    print("\nLevel:", lvl, "Exp:", exp % 10, "/", lvl * 10)
    if lvl >= 2:
        print("You leveled up")
    else:
        print("")
    enemy_num+=1

print("That's all I have for now lol, hope it's good enough to get an A :p")

# i didnt use any websites other than our in class work, i did ask my dad for help at some points tho.



