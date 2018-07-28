"""

6 Person Hunger Games (alpha) by Enine.

NOTE:Pvp has not been added yet. It is coming in a later update. For now, you can only die of natural causes, or by killing yourself.

SPLIT YOUR INPUTS INTO SEPERATE LINES AT INPUT BOX OR IT WILL NOT WORK!!!

12 or 24 person hunger games coming soon once I find an optimized system.

"""
import random
games = random.randint(1,1000)
playerlist = []

#the following creates tribute value, records name, adds to player list.

p1 = input("Tribute 1\'s name:")
print(p1)
playerlist.append(p1)
p2 = input("Tribute 2\'s name:")
print(p2)
playerlist.append(p2)
p3 = input("Tribute 3\'s name:")
print(p3)
playerlist.append(p3)
p4 = input("Tribute 4\'s name:")
print(p4)
playerlist.append(p4)
p5 = input("Tribute 5\'s name:")
print(p5)
playerlist.append(p5)
p6 = input("Tribute 6\'s name:")
print(p6)
playerlist.append(p6)

"""
the following functions are thungs that can happen to the tributes during the game. 
The argument 'guy' is replaced by a random tribute using the list. For example, when called: 
my_func(random.choice(playerlist))
"""

def make_fire(guy):
    print(guy + " made a fire.")
    print("- - - - - - - - - -")

def climb_tree(guy):
    print(guy + " climbed a tree.")
    print("- - - - - - - - - -")

def found_water(guy):
    print(guy + " found a stream with drinkable water. They take a sip to quench their thirst.")
    print("- - - - - - - - - -")

def cries(guy):
    print(guy + " curls up under a rock and cries themselves to sleep.")
    print("- - - - - - - - - -")

def eat_food(guy):
    print(guy + " eats some fresh food from a sponsor.")
    print("- - - - - - - - - -")
    
def ouch_leg(guy):
    print(guy + " trips on a root and twists their ankle.")
    print("- - - - - - - - - -")
    
def ouch_arm(guy):
    print(guy + " slips on a wet rock and sprains their wrist.")
    print("- - - - - - - - - -")
    
def ouch_head(guy):
    print(guy + " falls into a hidden pit and hits their head on a rock. " + guy + " stumbles away, disoriented.")
    print("- - - - - - - - - -")

def dogs(guy):
    print(guy + " narrowly escapes a pack of wild dogs.")
    print("- - - - - - - - - -")

def suicide(guy):
    print(guy + " couldn\'t take the pressure and ended their life.")
    playerlist.remove(guy)
    print("! ! ! ! !")
    print(guy + " is now out of the games. " + str(len(playerlist)) + " tributes remain.")
    print("! ! ! ! !")
    print("- - - - - - - - - -")

def poison(guy):
    print(guy + " gets poisoned by drinking  contaminated water.")
    playerlist.remove(guy)
    print("! ! ! ! !")
    print(guy + " is now out of the games. " + str(len(playerlist)) + " tributes remain.")
    print("! ! ! ! !")
    print("- - - - - - - - - -")
    
def cut(guy):
    print(guy + " got a deep cut and died from infection.")
    playerlist.remove(guy)
    print("! ! ! ! !")
    print(guy + " is now out of the games. " + str(len(playerlist)) + " tributes remain.")
    print("! ! ! ! !")
    print("- - - - - - - - - -")

def friends(guy,guy2):
    print(guy + " and " + guy2 + " form a temporary alliance.")
    print("- - - - - - - - - -")

events = [make_fire, climb_tree, found_water, cries, eat_food, suicide, dogs, ouch_leg, ouch_arm, ouch_head, cut, poison, ]

#____________

print("Your Tributes are " + p1 + ", " + p2 + ", " + p3 + ", " + p4 + ", " + p5 + ", and " + p6 + ".")

print("Let the " + str (games) + " Hunger games begin!")
print("....")
print("The gong sounds, and the tributes race to the cornucopia. After grabbing weapons and supplies, they dart into the woods.")
print("- - - - - - - - - -")
while len(playerlist) > 1:
    random.choice(events)(random.choice(playerlist))

print(playerlist[0] + " has won the "  + str(games) + " Hunger Games.")