import random

humans = ['knite', 'bishop', 'landlord']
humansOpts = {'knite': [100, 0.5], 'bishop': [80, 0.9], 'landlord': [120, 0.3]}
monsters = ['dragon', 'zombie', 'warlock']
monstersOpts = {'dragon' : [200, 0.8], 'zombie' : [150, 0.02], 'warewolf' : [100, 0.5]}
lastTurn = []

def checkArmieStatus(humans, monsters):
    if (humans and monsters):
        print("Let the war begins")
    else:
        if  not humans:
            print("Monsters WINS")
        else: 
            print("Humans WINS")

def whosTurn(lastTurn):
    if not lastTurn: 
        lastTurn = random.randint(0,1)
        return lastTurn
    return lastTurn

def turn(army, abilities):
    def chooseTheHealthiest(abilities):
        picked = {} 
        for key in abilities:
            picked[abilities[key][0]] = key
        chosen = sorted(picked).pop(-1)
        for key in picked:
            if key == chosen:
                ourHero = [picked[key], key]
        print(ourHero)
    chooseTheHealthiest(abilities)

def event_loop():
    checkArmieStatus(humans, monsters)
    newTurn = whosTurn(lastTurn)
    if newTurn :
        turn(humans, humansOpts)
    else:
        turn(monsters, monstersOpts)

event_loop()