# from random import Random
import random

last_dice = {}
players = {}
monsters = {}

def turn(player,health, nature):
    def dice():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1, dice3

    def hit_damage(health):
        if dice1 == dice2:
            damage = dice1*2
        else:
            damage = dice1 + dice2
        return health - damage

    dice1, dice2 = dice()
    last_dice[player] = "{} {}".format(dice1, dice2)
    print(player.title(), " diced: ", dice1, dice2)
    health = hit_damage(health)
    return player, health

def checkHealth(user, monster):
    
    
user, health = 'nspirit', 200
players = {user : health}
monster, mhealth = 'dragon', 100
monsters = {monster : mhealth}

def event_loop(players, monsters):
   while True:
       check = checkHealth(players[player], monsters[monster]) 
       if !check:
           break
        for player in players:
            if players[player] > 0:
                user, health = turn(player, players[player], "user")
                players = {user, health}
            else:
                print(player, "dead")
                break
        for monster in monsters:
            if monsters[monster] > 0:
                monster, health = turn(monster, monsters[monster], "monster")
                monsters = {monster, health}
            else:
                print(monster, "is dead!")
                break

event_loop(players, monsters)