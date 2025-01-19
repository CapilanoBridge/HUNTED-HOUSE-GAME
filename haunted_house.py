import random
 
def describe_room(room):
    
    if room == "entrance_hall":
        print("You are in the grand entrance hall. Dust motes dance in the single ray of moonlight filtering through a grimy window.")
        print("To the north, a wide staircase leads upwards. To the west, a heavy oak door beckons.")
    elif room == "living_room":
        print("You enter the living room. Cobwebs cling to the tattered velvet furniture. A cold draft chills you to the bone.")
        print("To the east, you see the entrance hall. To the south, a narrow passageway leads deeper into the house.")
    elif room == "dining_room":
        print("The dining room is a macabre sight. A long table is set with decaying food and tarnished silverware. A single candle flickers ominously.")
        print("To the north, you see the living room. To the west, a door leads to the kitchen.")
    elif room == "kitchen":
        print("The kitchen is a chaotic mess. Pots and pans lie scattered across the floor. A foul stench fills the air.")
        print("To the east, you see the dining room. To the south, a narrow staircase descends into darkness.")
    elif room == "basement":
        print("You descend into the dank basement. The air is thick with the smell of damp earth and decay. You hear a low, guttural growl...")
        print("To the north, you see the kitchen stairs.")
    elif room == "attic":
        print("You climb the creaking stairs into the attic. Dust motes swirl in the single shaft of moonlight. You hear a scratching sound overhead...")
        print("To the south, you see the entrance hall stairs.")
    else:
        print("You've entered an unknown part of the house.")
 
def get_player_choice():
    
    print("\nWhere do you want to go?")
    print("1. North")
    print("2. South")
    print("3. East")
    print("4. West")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
 
def move_player(current_room, choice):
    
    if current_room == "entrance_hall":
        if choice == 1:
            return "attic"
        elif choice == 4:
            return "living_room"
    elif current_room == "living_room":
        if choice == 2:
            return "dining_room"
        elif choice == 1:
            return "entrance_hall"
    elif current_room == "dining_room":
        if choice == 1:
            return "living_room"
        elif choice == 4:
            return "kitchen"
    elif current_room == "kitchen":
        if choice == 1:
            return "dining_room"
        elif choice == 2:
            return "basement"
    elif current_room == "basement":
        if choice == 1:
            return "kitchen"
    elif current_room == "attic":
        if choice == 2:
            return "entrance_hall"
    return current_room  # Stay in the same room if invalid choice
 
def check_game_over(current_room):
    
    if current_room == "basement":
        if random.randint(1, 5) == 1:  # 20% chance of encountering a monster
            print("You encounter a monstrous creature in the basement! You have been devoured!")
            return True
    return False
 
def play_game():
    
    current_room = "entrance_hall"
 
    while True:
        describe_room(current_room)
        choice = get_player_choice()
        next_room = move_player(current_room, choice)
 
        if check_game_over(next_room):
            break
 
        current_room = next_room
 
if __name__ == "__main__":
    play_game()
 