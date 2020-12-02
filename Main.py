# Ana Goglin
# I'm gonna try to make a game or something?
import random


# made each action into a function to make program more concise
def fight(action, eh):
    print("You chose to fight :0")
    if action == "sword":
        print("Hey good thing you're a sword, you do better at fight")
        # if and else inside an if else :0
        a = (lvl * 3)
    else:
        a = lvl * 2
    print("Wow you did", a, "damage!")
    damage = eh - a
    eh = damage
    if eh <= 0:
        return eh
    else:
        print("The Enemy now has", damage, "Health left\n")
        return eh


def trivia(j):
    print("There's only one questions and no multiple choice, good luck :) ")
    correct_answer = "twitter"
    # want to make more questions eventually (for next sprint thing tho)
    # make an array for multiple question options,
    # and a random number or something
    if j == "spell":
        print("The first letter is:", correct_answer[0])
    else:
        input("")
    answer = input(
        "What was Twitter's original name? ")
    # make function for more answers/questions
    if answer.lower() == correct_answer:
        # i used .lower in case input is caps or any combo
        print("The dude is shook and cries in defeat, you win")
        return True
    else:
        print("They laugh at you and you die, RIP", name)
        return False


def sneak(j2):
    if j2 == "stealth":
        print("you try to sneak past, theres a 50% chance")
        chance = random.randint(0, 2)
    else:
        print("you try to sneak past, theres a 25% chance")
        chance = random.randint(0, 4)
    input("")
    if chance == 1:
        print("You've sneaked right past them :O")
        return True  # snuck past
    else:
        print("couldn't get away")
        return False


def monster(health, enhp):
    action = (input(
        "Your actions are: fight, beat them at a trivia question, "
        "or sneak past them. \nWhat would you like to do? "))
    while enhp > 0:
        # a while loop if input isn't one the the expected responses
        while (action != "fight") and (action != "trivia") and (
                action != "sneak") and (action != "run"):
            print("Check your spelling")
            action = str(
                input("What would you like to do? fight, trivia, or sneak "))
        if action == "fight":
            enhp = fight(job, enhp)
            if enhp == 0:
                print("\n\nCongratulations on defeating enemy1")
                break
        elif action == "trivia":
            if trivia(job):
                # uses the true/false if snuck to show the combat result
                # resource used: dad
                break
            else:
                break

        elif action == "sneak":
            if sneak(job):
                break
        else:
            print("cant run away from a trainer battle")
        if enemy_hp <= 0:
            return health
        print("they attacks, deals ", enemy_num, "damage")
        health -= enemy_num
        if health <= 0:
            return health
        else:
            print("You have", health - enemy_num, "health left")
            print("What next?")
            action = (input(""))
    return health


# while loop to keep in 'action zone' until the enemy is defeated

name = input("What's your name? ")
print("Hi", name, "this is a super generic text based fighty adventure game "
                  "with little fighty and no adventure :)")
print("(press enter to continue if unprompted)")
# asking their name and saying hi
job = input("What job would you like to have? spell, sword, or stealth? \n "
            "(will have not a lot of actual impact idk how to code that) \n")
# assigning variables
exp = 0
lvl = 1
attack = 0
hp = lvl * 10
lvl = lvl + (exp // 10)
print("Your level is:", lvl)
# using operators to use exp to determine level
print(
    "You're in a castle, or dungeon or something "
    "atmospherically fantasy game like that")
input("")
enemy_num = 1
# setting up an enemy, using its number to make its health, v simple
for x in range(0, 3):  # for loop to have 3 enemies be the same w/ less work
    print(
        "Omg! out of nowhere an conveniently also"
        "low level animal or monster appears!\n")
    print("This is enemy number", enemy_num, "out of 3")
    enemy_hp = (enemy_num + 2) * 2
    input("")
    hp = monster(hp, enemy_hp)
    if hp <= 0:
        print("You are dead")
        dead = 0
        break
    else:
        print("You won!! Congrats")
        exp = exp + enemy_num * 7
        lvl = lvl + (exp // (lvl * 10))
    print("\nLevel:", lvl, "Exp:", exp % 10, "/", lvl * 10)
    # this ugly mess of a print function is formatting the level/exp
    if lvl >= 2:
        print("You leveled up")
        hp = 15
    else:
        print("")
    enemy_num += 1
print("You beat all the enemies!, Wasn't that easy peasy?")
input("You've reached the end of the game, only 0.01% of people were able to")


print("That's all I have for now  hope it's good enough to get an A :)")

# i did not use any websites other than our in class work,
# i did ask my dad for help at some points tho.
