game_over_cause = ""
win = False
print("The story begins.")
print("You start out in your house, you wake up from bed.")
decision1 = input("Do you want to get out of bed? It is 7 A.M. (Y/N)? : ")
if decision1.lower() == "y":
    print("You get out of bed and go to the kitchen to get some breakfast.")
    print("You see that a few plates are missing")
    print("However, you're too tired to pay it any mind.")
    decision2 = input("Would you like to go outside? (Y/N): ")
    if decision2.lower() == "y":
        print("You go outside, it's nice out.")
        print("You decide to go walking on the sidewalk.")
        decision3 = input("You hear something wrustling in the bushes, do you investigate? (Y/N): ")
        if decision3.lower() == "y":
            print("You investigate the bush.")
            print("It turns out it was a huge mountain lion trying to attract prey!")
            print("The mountain lion wastes no time and attacks you before you even see it.")
            game_over_cause = "lion attack"
        else:
            print("You choose to pay it no mind, was probably nothing anyways.")
            print("Someone else chose to investigate the bush and found it was a giant mountain lion, close call.")
            print("It appears aliens seem to be invading suddenly!")
            print("You wonder how bad this storytelling must be because of how chaotic everything is.")
            decision4 = input("Question more? Y/N: ")
            if decision4.lower() == "y":
                print("You ponder on about who would write something like this.")
                print("And also you're wondering why you're wondering about random questions while aliens are invading the world")
                print("One is standing infront of you right now.")
                print("This was always a dream of yours, which it ends up being as you wake up...")
                print("How unfortunate.")
                game_over_cause = "waking up"
            if decision4.lower() == "n":
                print("You choose not to overthink everything and run back to your house to seek shelter from the aliens.")
                print("Luckily, you've always dreamed of this happening so you prepared a stockpile for this exact situation!")
                print("Oh, how lucky! There must be years worth of supplies in here!")
                print("Or at least that's what you thought, because it's all vanished out of nowhere...")
                print("That went well didn't it, now whatever took your supplies locked you down here in your basement.")
                print("It's solid concrete walls everywhere you go, the aliens soon break in and take you with them to study in their lab")
                game_over_cause = "alien abduction"
    else:
        print("It's nice out, but you would rather watch the news so you can get up-to-date on world events.")
        print("A mountain lion runs alone the sidewalk outside, good thing you weren't out there!")
        print("Finally you remember the plates missing in the kitchen from when you woke up.")
        decision3 = input("Investigate where the plates went? (Y/N): ")
        if decision3.lower() == "y":
            print("You choose to investigate the suspected plate thief.")
            print("You find your plates in your basement on the floor for some reason.")
            print("You ponder about how and why the plates are down here when the door behind you shuts and locks")
            print("You choose not to panic because you have some supplies you left down here in case of a particular event.")
            print("However, all of the supplies are gone.")
            print("There seems to be a lot of commotion outside, though you can't tell what's going on because you don't have any windows down here.")
            print("Soon enough, a group of aliens break into your basement and take you away to a far away planet...")
            game_over_cause = "alien abduction"
        else:
            print("You don't really care about what happened to the plates, it was just a few anyways.")
            print("You see a small little creature scuttle by carrying a bag.")
            print("You seize the creature and see it was trying to steal your emergency supplies from the basement")
            print("You think to yourself how lucky you are to have caught it, you throw it outside and lock your doors and windows.")
            print("It looked like a small little alien, and soon enough what you can only assume is its colony starts landing outside.")
            print("You hear the news people in a state of panic as they try to explain the situation.")
            print("However, you've made the right decisions and secure your house before they can get in.")
            print("Then you watch as the world outside slowly becomes a subject of an alien civilization...")
            print("That's not your issue though, you have years worth of supplies that you kept on you.")
            print("Congratulations, survivor, you win!")
            win = True
else:
    print("You sleep another few hours and find a group of massive aliens standing above your bed.")
    print("You aren't in your bedroom anymore, you're in some alien spaceship about to be studied...")
    print("How unfortunate, you would've been so well prepared for this if you woke up in time...")
    game_over_cause = "alien abduction"

if win == False:
    print("Game over")
    print("Your adventure seemed to end way too soon due to " + game_over_cause + ", maybe you can learn from your mistakes...")
else:
    print("Congratulations, against all odds you intercepted the aliens' plans to take over your home and survived the invasion, for now at least.")
    print("Part two soon?")