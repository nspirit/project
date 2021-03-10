import random

humans = ['knite', 'bishop', 'landlord']
humansOpts = {'knite': [100, 0.5], 'bishop': [80, 0.9], 'landlord': [120, 0.3]}
monsters = ['dragon', 'zombie', 'warlock']
monstersOpts = {'dragon' : [100, 0.8], 'zombie' : [80, 0.02], 'warlock' : [100, 0.5]}
lastTurn = None 

def checkArmieStatus(humans, monsters):
    if (len(humans) == 0):
        print("Monsters WINS")
        return False 
    elif (len(monsters) == 0):
        print("Humans WINS")
        return False 
    else:
        # print("Let the war begins")
        return True 

def whosTurn(lastTurn):
    if lastTurn == None: 
        lastTurn = random.choice([True, False])
        return lastTurn
    else:
        if lastTurn == True:
            lastTurn = False
        else:
            lastTurn = True
        return lastTurn



def turn(army, abilities, lastTurn):
    def chooseTheHealthiest(abilities, army):
        picked = {} 
        # пустой словарь
        for key in abilities:
            # перебор по словарю, где ключ - имя юнита, а значение - список абилок
            picked[abilities[key][0]] = key
            # заполняем словарь. ключь - нулевой элемент списка - т.е. здоровье
            # а значение - имя юнита
        chosen = sorted(picked).pop(-1)
            # сортируем словарь, по ключу (а это здоровье) и сохраняем в chosen первый с конца элемент
            # потому что у него самое большое значение ключа, а это здоровье 
        for key in picked:
            # перебираем ключи в picked, где здоровье : имя_юнита
            if key == chosen:
                # если ключь, т.е. здоровье равно самому то, что выбрали уже выше, то делаем 
                # героя - из picked[key] - имя юнита, Key - Здоровье
                ourHero = [picked[key], key]
        return ourHero


    def diceToDamage():
        dice1 = random.randint(1,6) 
        dice2 = random.randint(1,6)
        if dice1 == dice2:
            return dice1*4 
        else:
            return dice1 + dice2

    def damageCalc(ourHero, damage, army):
        aliveOrDead = int(ourHero[1] - damage)
        if aliveOrDead > 0:
            ourHero[1] = aliveOrDead
            abilities[ourHero[0]][0] = ourHero[1]

        else:
            print(ourHero[0], " is dead.")
            abilities[ourHero[0]][0] = 0 
            army.remove(ourHero[0])


    ourHero = chooseTheHealthiest(abilities, army)
    damage = diceToDamage()
    print("Our hero is ", ourHero)
    print("He will get damage: ", damage)
    print("He is from the army", army)
    damageCalc(ourHero, damage, army)
    

def event_loop(lastTurn, humans, monsters):
    while True:
        print(humans, monsters)
        checkThem = checkArmieStatus(humans, monsters)
        if checkThem:
            lastTurn = whosTurn(lastTurn)
            if lastTurn:
                turn(humans, humansOpts, lastTurn)
            else:
                turn(monsters, monstersOpts, lastTurn)
        else:
            break

event_loop(lastTurn, humans, monsters)