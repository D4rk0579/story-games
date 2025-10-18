from random import choice
game_over_cause = ""
food_supply = 100
stamina = 100
days = 0
print("Welcome back to the game.")
print("I'm sure you've played part 1, so there shouldn't be any need for explaining.")
decision1 = input("Correct? (Y/N): ")
if decision1.lower() == "y":
    days +=1
    print("Good, good, we can begin.")
    print("Day 1")
    print("Now, let's wait for something interesting to happen.")
    print("3 hours later... (probably, not like you can tell time down here)")
    event1_list = ["A", "B", "C"]
    event1 = choice(event1_list)
    if event1 == "A":
        print("A group of aliens broke in and your defenses failed...unlucky.")
        game_over_cause = "aliens"
    elif event1 == "B":
        print("A group of aliens tried to break in but they made too much noise so you were well prepared and fought them off, nice!")
        print("However it did tire you out a bit, -25 stamina")
        stamina -= 25
    else:
        print("Aliens tried to break in but failed completely! Lucky you!")
    if game_over_cause == "": 
        move_on = input("Enter anything to continue to next day.")
        print("Day 2")
        days+=1
        food_supply -= 10
        print("Current stats: stamina: " + str(stamina) + "/100, food supply: " + str(food_supply) + "/100.")
        print("NOTE: by default you consume 10 food every day unless an event takes more of it.")
        event2_list = ["A", "B", "C"]
        event2 = choice(event2_list)
        if event2 == "A":
            print("You found a mouse eating at your food supply! Luckily, you scared it away pretty quickly. -10 food")
            food_supply -=10
            decision = input("Do you scare it away? Y/N: ")
            if decision.lower() == "y":
                outcome_list = ["survive", "don't", "don't"]
                outcome = choice(outcome_list)
                if outcome == "survive":
                    print("Phew, nothing else came from it so you're fine.")
                else:
                    print("How wonderful, a giant alien rat came out of the shadows and devoured you whole! Fantastic!")
                    game_over_cause = "alien rat"
            else:
                print("You were too scared to scare it away, so it ate a lot more of your food, but oh well!")
                food_supply -= 10
        elif event2 == "B":
            print("You find a backup TV you put down here, you turn it on to the news.")
            print("However, nobody is there, it's live but nobody is actually there to give the news")
            print("It makes you feel lonely, but doesn't have any real effects.")
        else:
            print("Nothing happened today. boring.")
            decision = input("Would you like to make it less boring by peeking out of your door? Y/N: ")
            if decision.lower() == "y":
                print("You saw something staring back at you, how nice! Oh wait...")
                game_over_cause = "horros beyond your imagination"
            else:
                print("For the best, who knows what could've been out there!")
        if game_over_cause == "":
            move_on = input("Enter anything to continue to next day.")
            print("Day 3")
            days += 1
            food_supply -= 10
            print("Current stats: stamina: " + str(stamina) + "/100, food supply: " + str(food_supply) + "/100.")
            print("There isn't anything you can hear going on outside anymore, it's rather peaceful actually.")
            decision = input("Would you like to venture out for more supplies? There is a risk, but the reward can be huge. The alternative is to get some much needed rest for the day. (Y/N): ")
            if decision.lower() == "y":
                print("You choose to take the adventure and head on outside.")
                event3_list = ["A", "B", "C"]
                event3 = choice(event3_list)
                if event3 == "A":
                    print("Wow! you found tons of food out here! best of all there were no dangerous encounters, so stamina loss was minimal!")
                    food_supply += 50
                    stamina -= 5
                elif event3 == "B":
                    print("You found a decent amount of food, enough to restock your supply, but you came pretty close to danger...")
                    food_supply = 100
                    stamina -= 15
                else:
                    print("Wow, that went horribly! You spent the whole time running around and found nothing!")
                    print("Oh, how wonderful! You got locked out of your own house! Congratulations comrade!")
                    game_over_cause = "house taken"
            else:
                print("You chose to sleep the whole day, recovering your stamina and not eating anything.")
                stamina = 100
            move_on = input("Enter anything to continue to next day.")
            days+=1
            print("Day 4")
            print("Current stats: stamina: " + str(stamina) + "/100, food supply: " + str(food_supply) + "/100.")
            if stamina < 50:
                print("You are really tired, so you decided to take a rest day today.")
                stamina = 100
            else:
                print("You have plenty of energy, so you try to expand out of your basement and manage to secure the rest of your house.")
                print("You found some extra food in your kitchen, just where you left it!")
                stamina = 25
                food_supply += 25
            move_on = input("Enter anything to continue to next day")
            food_supply -= 10
            print("Current stats: stamina: " + str(stamina) + "/100, food supply: " + str(food_supply) + "/100.")
            if stamina < 50:
                print("You're feeling tired today and take a rest day.")
            else:
                print("You have plenty of energy now, so you expand outside of your basement and secure your house.")
            move_on = input("Enter anything when you're ready to move on.")
            food_supply -= 10
            days+=1
            print("Current stats: stamina: " + str(stamina) + "/100, food supply: " + str(food_supply) + "/100.")
            print("Day 5")
            print("You've managed to secure the whole house, so you're in a great position. You can also finally tell time and sleep on an actual bed. Yay!")
            print("You also managed to grab some extra weaponry to defend yourself.")
            print("Your goals have been updated: Secure the town")
            print("You choose to sleep the day to ensure you're prepared for tomorrow, it'll be one chaotic day.")
        else:
            print("Game over")
            print("How unfortunate, it all ended so fast...")
            print("Ending cause: " + str(game_over_cause))
            print("do better next time!")
    else:
        print("Game over")
        print("How unfortunate, it all ended so fast...")
        print("Ending cause: " + str(game_over_cause))
        print("do better next time!")
else:
    print("Go play part 1 then!")
    game_over_cause = "not playing part 1 first"
if game_over_cause == "":
    print("Congratulations, you survived part 2! It's almost as bad as part 1, so that's quite the achievement!")