from random import choice, randint
exp_to_next = 10
exp = 0
level = 1
health = 25
damage = [2, 3, 4, 5]
max_dmg = damage[3] #default stats
game_over_cause = "" #checks for game over later, if you die it'll say how

def fight(player_hp, enemy_hp, enemy_type, damage): #fight system function
    while player_hp > 0 and enemy_hp > 0:
        player_turn = input("Attack or run away? (say 'attack' or 'a' to attack, anything else to run. ")
        if player_turn.lower() == "attack" or player_turn.lower() == "a": #checks player turn
            damage_dealt = choice(damage)
            print("You dealt " + str(damage_dealt) + " damage out of " + str(damage[3]))
            enemy_hp -= damage_dealt
            print("Enemy hp: " + str(enemy_hp)) #calculates damage and deals it
        else:
            escape_chance = [1, 2] #if you want to escape, you have a chance to fail.
            if choice(escape_chance) == 1:
                print("Escaped successfully.")
                break
            else:
                print("Failed to escape! Enemy caught you and dealt 2 extra damage.")
        if enemy_type == 1: #checks different enemy types, more will be added later, including possibly bosses.
            enemy_damage = [1, 2, 3]
            if randint(1, 50) == 2:
                print("The enemy did some super move out of nowhere and created a supermassive black hole!")
                player_hp -= 25
            else:
                damage_dealt = choice(enemy_damage)
                print("The enemy dealt " + str(damage_dealt) + " damage.")
                player_hp -= damage_dealt
                print("Your hp: " + str(player_hp)) #takes enemy damage and subtracts from player hp
        elif enemy_type == 2:
            enemy_damage = [2, 3, 4]
            damage_dealt = choice(enemy_damage)
            print()
            
        else:
            continue
    if player_hp > 0 and enemy_hp <= 0: #If true the player killed the enemy
        print("You won the fight!")
        return True
    elif player_hp > 0 and enemy_hp > 0: #If true the player escaped the fight
        print("You managed to escape successfully, however you didn't get anything.")
        return True
    else: #If true the player lost the fight
        print("You lost...")
        return False

def level_up(exp, exp_required, level, damage):
    if exp >= exp_required:
        print("You leveled up! Your damage has increased.")
        damage[0] += 1
        damage[1] += 1
        damage[2] += 1
        damage[3] += 1
        max_dmg = damage[3]
        print("Your new damage range:" + str(damage))
        exp -= exp_required #calculate any leftover exp
        exp_required*=1.5 #calculate a new level requirement
        print("Leftover exp: " + str(exp))
        print(print("New exp requirement: " + str(exp_required))) #print it out
    else:
        print("You aren't ready to level up yet.")
print("Welcome to part 3!")
print("This one is more complex than the others, since it also has a fight system along with progression.")
print("I'm too lazy to check if you've played the other 2 parts or not, you better have.")
print("Anyways, let's get back to where we left off.")
print()
print("You begin to make your way out of the house, you brought some extra supplies and a backpack with you.")
print("You must find a way to secure the neighborhood, and start an outpost for anyone else who happened to survive.")
print("Currently however, you are actually really weak and can barely lift a pebble, so good luck out there.")
while game_over_cause == "": #loops the game, makes it so I don't have to check for game over after every fight
    print()
    print("Current stats: Damage:" + str(damage[0])+"-"+str(damage[3]) + " Health: " + str(health))
    print()
    print("Day 6") #leaves off on the day the last game did
    print()
    print("You leave the safety of your home to face the world outside, it's all in ruins, you feel really disturbed seeing it's all a wasteland now...")
    print()
    print("Oh well, you push the thought out of your mind so you can focus on surving here.")
    print("Almost immediately, a small alien shows up, looking for a fight.") #story
    move_on = input("Enter anything to continue.")
    if fight(health, 5, 1, damage) == True:
        exp += 10
        level_up(exp, exp_to_next, level, damage)
    else:
        game_over_cause = "complete loseritis, like imagine losing to the tutorial enemy, how does that even happen?"
        break
    print()
    print()
    print("Congratulations on winning that fight, you even feel a tad stronger now, and can maybe begin lifting pebbles!")
    print()
    print("Anyways, you begin to secure the immediate area, rebuilding your broken fence you built around your yard.")
    print("You ate some of your food supply, recovering your health back.")
    health = 25 #story progression
    print()
    print()
    moveon = input("Enter anything to continue.")
    print()
    print("Day 7 (dang it's been a week already)")
    print()
    print("The sky has turned a dark orange now, reminds you of all of those apocalypse movies.")
    print("Scary, isn't it? How such a thriving old town was reduced to ruins in such a short amount of time...")
    print("Everybody who once lived here is somewhere else now, nobody really knows where, but they're there.")
    print("You look at the tree and it reminds you of your old life, how depressing.")
    print("In the middle of your pondering, another alien sneaks up on you, one slightly stronger than the last one. Time to fight I guess.")
    if fight(health, 10, 2, damage) == True:
        exp = 0
        exp_to_next = 22.5
        print("You leveled up! Your damage has increased.")
        damage[0] += 1
        damage[1] += 1
        damage[2] += 1
        damage[3] += 1
        max_dmg = damage[3]
        print("Your new damage range:" + str(damage))
        print("Leftover exp: " + str(exp))
        print(print("New exp requirement: " + str(exp_to_next))) #print it out
    else:
        game_over_cause = "Died to an alien fight, pretty early one too."
        break
    break
if game_over_cause != "": #you lost
    print("Your adventure ended way too soon...")
    print("Cause of death: " + str(game_over_cause))
else: #you won or just got to the end of the game
    print("Congratulations, finished the game!")