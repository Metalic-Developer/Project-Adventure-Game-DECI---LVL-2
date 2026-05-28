import time
import sys
import random

# Write The Code As If Someone Is Typing It
def dramatic_print(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print()
    print("\n")

# Print The Choices
def choices(choice1, choice2):
    print("Choice 1: " + choice1)
    print("Choice 2: " + choice2)
    print("What would you like to do?")
    return input("(Please enter 1 or 2) ")

# First Game
def first_game():
    start = time.time()
    max_time = 100

    # Timer
    def timer():
        elapsed_time = time.time() - start
        if elapsed_time >= max_time:
            dramatic_print("\nTime Is enough")
            return "no"
        else:
            return "ok"

    total_score = 10

    # This Will Be Used After Each Level
    def stats(currentLevel):
        print("\n")
        print("=> " + currentLevel)
        print("Total Score: " + str(total_score))
        print("\n")

    # Intro Level:
    print("===============================")
    print("== The Lost Pyramid's Secret ==")
    print("===============================")

    # The Description Of The Level
    dramatic_print(
        "\nYou awaken in a dusty tomb, a dull throbbing in your head, No memory of how you arrived. \
Disoriented, you sit up and find yourself on a cold, hard stone floor. \n\
Sand clinging to your clothes, Musty air fills your lungs, \
and flickering torches paint an eerie glow on the ancient walls. \n\
A faint glimmer ahead beckons you forward.\n"
    )

    # This Code Is Used To Print Some Terms The Player Must Know
    dramatic_print(
        "=> INSTRUCTIONS\n\
    Health Points (total_score): It represents your character's ability to withstand attacks\n\
    Inventory: It will hold items found during the adventure\n\
    Score: It tracks your success throughout the game\n\
    -> If You Want To Exit The Game Press \"q\""
    )

    stats("ENTRY LEVEL STATS")

    # Choice Piont No.1
    choice_point_1 = choices(
        "Panicked, you scramble to your feet and blindly charge \
towards the nearest passage, hoping it leads out. (Go to Descent)",
        "Taking a deep breath, you assess your surroundings. \
You notice a satchel lying beside you. It might hold something useful. (Go to Inventory)",
    )

    # While Loop Is Use To Avoid Entering A Wrong Input
    while True:
        # Choice 1
        if choice_point_1 == "1":
            dramatic_print(
                "You open the satchel. Inside, you find a dented lantern,\n\
a worn leather pouch filled with what appears to be dried fruit,\n\
and a small, intricately carved amulet."
            )

            if timer() == "ok":
                print("Time Is Enough")
                break

            # Choice Piont No.2
            choice_point_2 = choices(
                "You light the lantern and cautiously explore the tomb, hoping to find a way out. (Go to Exploration)",
                "The amulet feels strangely warm in your hand. You decide to examine it closer. (Go to Amulet)",
            )
            while True:
                # Choice 1
                if choice_point_2 == "1":
                    dramatic_print(
                        "Lantern in hand, you navigate the tomb's corridors. \n\
You come across a series of ancient murals depicting a forgotten ritual. \n\
One scene shows a figure placing the same amulet you hold on a pedestal at the end of the chamber."
                    )

                    if timer() == "ok":
                        print("Time Is Enough")
                        break

                    # Choice Piont No.3
                    choice_point_3 = choices(
                        "Intrigued by the murals, you decide to follow the depicted ritual\n\
                            and place the amulet on the pedestal. (Go to Ritual).",
                        "Something about the ritual feels unsettling. You choose to explore a different passage. (Go to Passage)",
                    )
                    while True:
                        # Choice 1
                        if choice_point_3 == "1":
                            dramatic_print(
                                "As you place the amulet on the pedestal, a deep rumbling echoes through the tomb.\n\
The air shimmers, and a hidden passage materializes before you.\
A sense of relief washes over you - a way out!\n\n\
Entering the passage, you find yourself in a long, descending corridor.\n\
The air here is fresher, cleaner, hinting at an exit above. You press on, lantern held high."
                            )

                            if timer() == "ok":
                                print("Time Is Enough")
                                break

                            # Choice Piont No.4
                            choice_point_4 = choices(
                                "Sticking to your goal, you continue down the main passage,\
eager to reach the surface. (Go to Ascent).",
                                "You hear a faint trickle of water further down the passage.\n\
Intrigued, you veer off the main path to investigate. (Go to Water Source).",
                            )
                            while True:
                                # Choice 1
                                if choice_point_4 == "1":
                                    dramatic_print(
                                        "Following the sound, you find a hidden chamber with a small spring bubbling up from the ground.\n\
Relief washes over you - you can replenish your dwindling water supply.\n\
However, as you lean down to drink, a swarm of translucent insects erupts from the water, stinging your exposed skin.\
Penalty: You lose some health and have to move slower due to the stings. (Return to Ritual with the penalty)"
                                    )
                                    total_score = 0
                                    stats("First Level")

                                    print("Game Over")
                                    break

                                # Choice 2
                                elif choice_point_4 == "2":
                                    dramatic_print(
                                        "Ignoring distractions, you reach the end of the passage. \
A heavy stone door stands before you. Relief washes over you - the exit!"
                                    )

                                    if timer() == "ok":
                                        print("Time Is Enough")
                                        break

                                    # Choice Piont No.5
                                    choice_point_5 = choices(
                                        "You push against the door with all your might. It doesn't budge. (Go to Lever)",
                                        "Looking around, you see a series of levers embedded in the wall beside the door. (Go to Lever)",
                                    )
                                    while True:
                                        # All Choices Have The Same Result
                                        if choice_point_5 == "1" or choice_point_5 == "2":
                                            dramatic_print(
                                                "You inspect the levers. One of them seems slightly out of place. Taking a chance, you pull it.\n\
A grinding sound fills the chamber, and the stone door slowly creaks open."
                                            )
                                            dramatic_print(
                                                "Blinking in the sunlight, you step out of the tomb.\n\
Fresh air fills your lungs, and the sound of birdsong replaces the tomb's oppressive silence. You have escaped!"
                                            )
                                            dramatic_print(
                                                "Congratulations! You have successfully navigated the tomb and reached freedom."
                                            )
                                            break
                                        elif choice_point_5 == "q":
                                            break
                                        else:
                                            print("\nInvalid Input")
                                            if timer() == "ok":
                                                print("Time Is Enough")
                                                break
                                            choice_point_5 = choices(
                                                "You push against the door with all your might. It doesn't budge. (Go to Lever)",
                                                "Looking around, you see a series of levers embedded in the wall beside the door. (Go to Lever)",
                                            )

                                    break
                                elif choice_point_4 == "q":
                                    break
                                else:
                                    print("\nInvalid Input")
                                    if timer() == "ok":
                                        print("Time Is Enough")
                                        break
                                    choice_point_4 = choices(
                                        "You hear a faint trickle of water further down the passage.\n\
                                        Intrigued, you veer off the main path to investigate. (Go to Water Source).",
                                        "Sticking to your goal, you continue down the main passage, eager to reach the surface. (Go to Ascent).",
                                    )
                        # Choice 2
                        elif choice_point_3 == "2":
                            dramatic_print(
                                "Panicked, you scramble to your feet and blindly charge towards the nearest passage,\n\
hoping it leads out. You sprint through the darkness, adrenaline coursing through your veins.\n\
The air grows stale, the passage narrows further. Suddenly, the floor gives way beneath you.\n\
You plummet into a seemingly bottomless pit."
                            )

                            dramatic_print(
                                "You land hard on a rocky ledge, momentarily stunned.\n\
You scramble to your feet, but the fall has broken your lantern.\n\
There's only darkness below."
                            )

                            total_score = 2
                            stats("Thrid Level Stats")

                            if timer() == "ok":
                                print("Time Is Enough")
                                break

                            # Choice Piont No.4
                            choice_point_4 = choices(
                                "try to climb back up",
                                "press on into the unknown depths",
                            )
                            while True:
                                # Choice 1
                                if choice_point_4 == "1":
                                    dramatic_print(
                                        "With only the faint echo of your own ragged breaths for company, you press on,\
feeling your way along the damp walls. The air grows thick and heavy, making it hard to breathe.\
The silence is broken only by the occasional drip of water. After what feels like an eternity,\
you reach a dead end. The passage crumbles to dust before you.\n\nGame Over"
                                    )

                                    total_score = 0
                                    stats("Thrid Level Stats")

                                    break
                                # Choice 2
                                elif choice_point_4 == "2":
                                    dramatic_print(
                                        "Scrambling for handholds, you attempt to climb back up.\n\
Your fingers strain against the rough stone, but your grip isn't strong enough.\n\
Exhausted and with a growing sense of dread, you realize you're trapped.\n\nGame Over"
                                    )

                                    total_score = 0
                                    stats("Thrid Level Stats")

                                    break
                                elif choice_point_4 == "q":
                                    break
                                else:
                                    print("\nInvalid Input")
                                    if timer() == "ok":
                                        print("Time Is Enough")
                                        break
                                    choice_point_4 = choices(
                                        "try to climb back up",
                                        "press on into the unknown depths",
                                    )

                            break
                        elif choice_point_3 == "q":
                            break
                        else:
                            print("\nInvalid Input")
                            if timer() == "ok":
                                print("Time Is Enough")
                                break
                            choice_point_3 = choices(
                                "You hear a faint trickle of water further down the passage.\n\
                                Intrigued, you veer off the main path to investigate. (Go to Water Source).",
                                "Sticking to your goal, you continue down the main passage, eager to reach the surface. (Go to Ascent).",
                            )
                    break
                # Choice 2
                elif choice_point_2 == "2":
                    dramatic_print(
                        "You stare intently at the amulet, mesmerized by its intricate carvings. \n\
You feel a strange pull, a compulsion to touch the central symbol. As you do, \n\
a searing pain shoots through your arm, and the tomb begins to tremble violently.\n\
Injured, you are forced to explore the tomb in pain. Go back to Exploration with a penalty"
                    )

                    total_score = 5
                    stats("Second Level Stats")

                    if timer() == "ok":
                        print("Time Is Enough")
                        break

                    choice_point_2 = "1"
                elif choice_point_2 == "q":
                    break
                else:
                    print("\nInvalid Input")

                    if timer() == "ok":
                        print("Time Is Enough")
                        break

                    choice_point_2 = choices(
                        "You light the lantern and cautiously explore the tomb, hoping to find a way out. (Go to Exploration)",
                        "The amulet feels strangely warm in your hand. You decide to examine it closer. (Go to Amulet)",
                    )
            break
        # Choice 2
        elif choice_point_1 == "2":
            dramatic_print(
                "You sprint through the darkness, adrenaline coursing through your veins. \n\
The passage narrows, the air grows stale. Suddenly, the floor gives way beneath you. \n\
You plummet into a pit filled with skeletal remains.\n\nGame Over"
            )

            total_score = 0
            stats("First Level Stats")

            break
        elif choice_point_1 == "q":
            break
        else:
            print("\nInvalid Input")
            if timer() == "ok":
                print("Time Is Enough")
                break
            choice_point_1 = choices(
                "Panicked, you scramble to your feet and blindly charge \n\
                towards the nearest passage, hoping it leads out. (Go to Descent)",
                "Taking a deep breath, you assess your surroundings. \n\
                You notice a satchel lying beside you. It might hold something useful. (Go to Inventory)",
            )


def second_game():
    max_time = 600
    start = time.time()

    # Timer
    def timer():
        elapsed_time = time.time() - start
        if elapsed_time >= max_time:
            dramatic_print("\nTime Is enough")
            return "no"
        else:
            return "ok"

    total_score = 10

    # This Will Be Used After Each Level
    def stats(current):
        print("\n")
        print("Current Level:", current)
        print("Total Score: " + str(total_score))
        print("\n")

    # Intro Level:
    print("===============================")
    print("====== The Ocean's Mith =======")
    print("===============================")

    # The Description Of The Level
    dramatic_print("You awaken with a jolt, the rhythmic creaking of old wood filling your ears.\n\
Disoriented, you sit up and find yourself on a rickety wooden boat, the salty spray stinging your face.\n\
Your head throbs, and your past is a swirling fog. In your hand, you clutch a weathered map,\n\
its edges frayed and symbols cryptic.  A single inscription burns into your mind: \"The Ocean's Myth.\"\n\
Legends whisper of a lost underwater city, brimming with forgotten knowledge and untold treasures.")

    # This Code Is Used To Print Some Terms The Player Must Know
    dramatic_print(
        "=> INSTRUCTIONS\n\
    Health Points (total_score): It represents your character's ability to withstand attacks\n\
    Inventory: It will hold items found during the adventure\n\
    Score: It tracks your success throughout the game\n\
    -> If You Want To Exit The Game Press \"q\""
    )

    stats("Intro Level")

    # First Level:
    # Choice Piont No.1
    choice_point_1 = choices("Panicked by your amnesia and the desolate surroundings,\n\
you impulsively steer the boat towards the nearest landmass on the horizon. (Go to Uncharted Shores).",
        "Set sail immediately, fueled by the thrill of the hunt and the promise of untold riches. (Go to Departure)")

    while True:
        # Choice 1
        if choice_point_1 == "1":
            dramatic_print("Driven by fear, you push the rickety boat towards the distant landmass.\n\
As you get closer, the once inviting coast reveals itself to be a treacherous cliff face.\n\
The unforgiving waves smash your vessel against the rocks, sending you plunging into the churning sea.\n\n Game Over")

            total_score = 0
            stats("First Level")

            break

        # Choice 2
        elif choice_point_1 == "2":
            dramatic_print("You scour the boat's meager supplies, finding a half-empty waterskin, some stale crackers,\n\
and a surprisingly well-preserved spyglass. Tucked in a hidden compartment, you discover a tattered journal with a single entry:\n\
\"The Ocean's Myth lies hidden beneath the waves. Follow the stars and the song of the whales.\"")

            if timer() == "ok":
                print("Time Is Enough")
                break

            # Choice Piont No.2
            choice_point_2 = choices("The cryptic message sparks your curiosity.\n\
You decide to follow the map and the journal's clues. (Go to Following the Clues).",
                "The vastness of the ocean fills you with dread. You abandon the map and the whispers of a lost city,\n\
desperately searching for a passing ship. (Go to Distress Signal).")

            while True:
                # Choice 1
                if choice_point_2 == "1":
                    dramatic_print("Armed with the map and the journal's cryptic message,\n\
you set a course guided by the constellations and the haunting calls of whales echoing in the distance.\n\
Days turn into weeks, your rations dwindling. Hope begins to dwindle with the supplies.")

                    if timer() == "ok":
                        print("Time Is Enough")
                        break

                    choice_point_3 = choices("Just as you're about to give up, a pod of whales breaches the surface, circling your boat.\n\
Following their lead, you steer towards a cluster of storm clouds on the horizon. (Go to Storm's Embrace)",
                        "Unable to decipher the whales' message, you continue on your original course,\n\
your resolve weakening with each passing day. (Go to Desolation).")
                    while True:
                        # Choice 1
                        if choice_point_3 == "1":
                            dramatic_print("Hesitantly, you navigate towards the churning storm clouds.\n\
As you enter the heart of the tempest, the sky opens up, revealing a breathtaking sight:\n\
a colossal underwater city bathed in an ethereal glow, protected by a swirling vortex. The Ocean's Myth!")

                            if timer() == "ok":
                                print("Time Is Enough")
                                break

                            # Choice Point No.4
                            choice_point_4 = choices(
                                "Awe-struck, you sail directly towards the city, eager to explore its secrets. (Go to The City's Embrace)",
                                "Cautious of the swirling vortex, you circle the perimeter, searching for a safe entrance. (Go to Hidden Passage)")

                            while True:
                                # Choice 1
                                if choice_point_4 == "1":
                                    dramatic_print("Ignoring the churning vortex, you steer straight for the city.\n\
A colossal wave crashes against your boat, tossing you high into the air before plunging you into the depths.\n\
The immense pressure crushes the rickety vessel, and the darkness claims you.\n\nGame Over")
                                    break
                                # Choice 2
                                elif choice_point_4 == "2":
                                    dramatic_print("Carefully navigating the perimeter, you spot a faint bioluminescent glow emanating from a crevice in the rocks.\n\
Following the faint light, you discover a narrow tunnel leading into the heart of the city.")
                                    dramatic_print("Part 2: The Ocean's Myth (This is where the true challenges begin - navigating the underwater city,\n\
solving puzzles to gain access to its forgotten knowledge, and perhaps even facing guardians protecting its secrets).\n\
The successful resolution of these challenges will lead to the happy ending.")

                                    dramatic_print(
                                        "Here's a glimpse of a possible happy ending:\n\nHaving outsmarted the city's")
                                    break
                                elif choice_point_4 == "q":
                                    break
                                else:
                                    print("\nInvalid Input")
                                    if timer() == "ok":
                                        print("Time Is Enough")
                                        break
                                    choice_point_4 = choices(
                                        "Awe-struck, you sail directly towards the city, eager to explore its secrets. (Go to The City's Embrace)",
                                        "Cautious of the swirling vortex, you circle the perimeter, searching for a safe entrance. (Go to Hidden Passage)")
                            break
                        # Choice 2
                        elif choice_point_3 == "2":
                            dramatic_print("Days turn into weeks, and the vast emptiness of the ocean stretches before you.\n\
Your supplies are depleted, and hope dwindles. Just as you're on the verge of succumbing to despair,\n\
a speck appears on the horizon - a ship!")

                            dramatic_print("Waving frantically, you signal the approaching vessel.\n\
Relief washes over you as they pull alongside. However, the pirates aboard sneer and relieve you of your meager possessions\n\
before leaving you adrift once more.\n\nGame Over")

                            total_score = 0
                            stats("Third Level")

                            break
                        elif choice_point_3 == "q":
                            break
                        else:
                            print("\nInvalid Input")
                            if timer() == "ok":
                                print("Time Is Enough")
                                break
                            choice_point_3 = choices("Just as you're about to give up, a pod of whales breaches the surface, circling your boat.\n\
Following their lead, you steer towards a cluster of storm clouds on the horizon. (Go to Storm's Embrace)",
                                "Unable to decipher the whales' message, you continue on your original course,\n\
your resolve weakening with each passing day. (Go to Desolation).")
                # Choice 2
                elif choice_point_2 == "2":
                    dramatic_print("\n\nGame Over")

                    total_score = 0
                    stats("Second Level")

                    break
                elif choice_point_2 == "q":
                    break
                else:
                    print("\nInvalid Input")
                    if timer() == "ok":
                        print("Time Is Enough")
                        break
                    choice_point_2 = choices("The cryptic message sparks your curiosity.\n\
You decide to follow the map and the journal's clues. (Go to Following the Clues).",
                        "The vastness of the ocean fills you with dread. You abandon the map and the whispers of a lost city,\n\
desperately searching for a passing ship. (Go to Distress Signal).")
            break
        elif choice_point_1 == "q":
            break
        else:
            print("\nInvalid Input")
            if timer() == "ok":
                print("Time Is Enough")
                break
            choice_point_1 = choices("Panicked by your amnesia and the desolate surroundings,\n\
you impulsively steer the boat towards the nearest landmass on the horizon. (Go to Uncharted Shores).",
                "Set sail immediately, fueled by the thrill of the hunt and the promise of untold riches. (Go to Departure)")

# This is The Start Of The Game
def main():
    # Working With The Random Library
    game = "".join(random.choices(["first", "second"]))

    if game == "first":
        first_game()
    else:
        second_game()

    play_again = input("Do You Want To Play Again? (n/y) ")
    while True:
        # Continue
        if play_again == "y":
            dramatic_print("\nOk. Let's Get Started:\n")

            # This Makes The Function Repeat Itself
            main()
        # Exit:
        elif play_again == "n":
            dramatic_print("Goodbye")
        else:
            print("\nInavalid Input")
            play_again = input("Do You Want To Play Again? (n/y) ")

# This Is The Game:
main()
