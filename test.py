import random

humans = ['knite', 'bishop', 'landlord']
humansOpts = {'knite': [100, 0.5], 'bishop': [80, 0.9], 'landlord': [120, 0.3]}
monsters = ['dragon', 'zombie', 'warewolf']
monstersOpts = {'dragon' : [200, 0.1], 'zombie' : [150, 0.02], 'warewolf' : [100, 0.5]}
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
            print(key)
            print(abilities[key][0])
            picked = {key : abilities[key][0]}
            # if picked:
            #     if picked[0][0] > {key, abilities[key][0]}:
            #         pass
            #     else:
            #         picked = {key : abilities[key]}
            # else:
            #     picked = {key : abilities[key]}
        print(picked) 
    chooseTheHealthiest(abilities)

def event_loop():
    checkArmieStatus(humans, monsters)
    newTurn = whosTurn(lastTurn)
    if newTurn :
        turn(humans, humansOpts)
    else:
        turn(monsters, monstersOpts)

event_loop()