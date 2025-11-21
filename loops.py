
# Name: Jerrod Bolton
# Date: Nov 20,2025
# Python class 235 Programming I - Assignment Function and Loops
# For the assignment, I'll be adding functions and loops to my maze game. this is so that the # gamer don't have to start over every time they make a wrong move.

# I would like to make a program that simulates a simple Maze game. Where a people can navigate through a maze using text commands.

character_detail = []
# This is a function that allows the user to navigate through the maze.
def  maze_navigation():
    print("=======================================================")
    print("You are in round one of the maze. You can move north, south, east, or west.")
    print("Let's see if you can find your way through the maze!")
    print("=======================================================")
    start = input("Would you like to start the game (yes/no): ").lower()

    # the correct answers to get through the maze are south, west, east, north.

    if start == 'yes' or start == 'y':
        directions = input("Round 1: What directions would like to go? (north/south/east/west): ").lower()

  
    # Now I need to make the first round that the user will play through. But it need to keep going until the right direction is chosen is given.

    # This is the first round that the user will play through.
    # In this round the user needs to go south to move to the next round.
    # Once the user inputs south they will move to round two b/c the while loop will end.
    # this is a wile loop for round one of the maze game. that will continue until the right direction is given which is south. 
        while directions != "south":
            print("You moved", directions, "and found a dead end. Try again!")
            directions = input("What directions would like to go? (north/south/east/west): ").lower()
        
        print("=======================================================")
        print("          You moved south and move to round two!"       )
        print("=======================================================")

        directions = input("Round 2: What directions would like to go? (north/south/east/west): ").lower()

    # Now I need to make the second round that the user will play through. But it need to keep going until the right direction is chosen is given.
    #  this is a wile loop for round two of the maze game.
    
        while directions != "west":
            print("You moved", directions, "and found a dead end. Try again!") 
            directions = input("What directions would like to go? (north/south/east/west): ").lower()
            print("=======================================================")

        print("=======================================================")
        print("   You moved", directions, "and move to round three!   ")
        print("=======================================================") 

        directions = input("Round 3: What directions would like to go? (north/south/east/west): ").lower()

    
        while directions != "east": 

            print("You moved", directions, "and found a dead end. Try again!") 
            print("=======================================================")
            directions = input("What directions would like to go? (north/south/east/west): ").lower()
          
        print("=======================================================")
        print("   You moved", directions, "and move to round four!   ")
        print("=======================================================") 

        while directions != "north":
            print("You moved", directions, "and found a dead end. Try again!") 
            print("=======================================================")
            directions = input(" Round 4: What directions would like to go? (north/south/east/west): ").lower()

        print("=======================================================")
        print(" You moved", directions, "and found yourself back at the started in the maze. Exactly where you need to be! Live large! Be happy, and play again if you need.")
 # this is a else the last part of the maze game. 
    else:
        print("You chose not to start the game. Goodbye!")
        
def create_character():  
    # I also would lie to save the character details to a text file. 
    # Saving the character by name went a person is playing. 

    save_character = input("Would you like to save your character? (yes/no): ")
    if save_character == 'yes' or save_character == 'y':
        # This section collects character details from the user.    
        character_name =  input("What is your character's name? :  ")
        character_gender = input("What is the gender of the your character? : ")
        character_design = input("Describe your character's appearance: ") 
        character_origin = input("Where does your character come from? : ")
        character_eye_color = input("What is your character's eye color? :   ")
        character_hair_color = input("What is your character's hair color? :  ")
        character_age = input("How old is your character? ")

        print("=======================================================") 
        with open("character_saver", "a") as file:
            # This writes the character information to the file.
            file.write("--------------------------------------------------\n")
            file.write(f"Character Name: {character_name}\n")
            file.write("--------------------------------------------------\n")      
            file.write(f"Character Gender: {character_gender}\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Character Appearance: {character_design}\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Character Origin: {character_origin}\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Character Eye Color: {character_eye_color}\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Character Hair Color: {character_hair_color}\n")
            file.write("--------------------------------------------------\n")
            file.write(f"Character Age: {character_age}\n")
            file.write("--------------------------------------------------\n")

            print(f"Your character {character_name} has been saved to the file character_saver.txt.")  
            print("=======================================================")
            # Confirmation message this is telling people that their character has been created.
            print(f"Great! Your character {character_name} has been created.")
            print("          Now, let's navigate through the maze!"        )
            print("=======================================================")

        character_detail.append(character_name)
        character_detail.append(character_design)
        character_detail.append(character_origin)
        character_detail.append(character_eye_color)
        character_detail.append(character_hair_color)
        character_detail.append(character_age)


    else:
        print("You chose not to save your character.")


print("=======================================================")
# this is ust something to add some space before the title of the program.
print("           Welcome to the Maze Simulator!              ")
print("Where you can fond your way through the maze, and exit!")
print("=======================================================")
# This function allows the user to navigate through the maze.
print("Let's start by creating your character for the maze adventure!")
print("=======================================================")


character_is_made = input("Do you have a character saved? If not, let's create one together!: (yes/no): ")

if character_is_made == 'yes' or character_is_made == 'y':
  print("Great! Let's proceed to the maze navigation.")
# This calling the function allows the user to navigate through the maze.
  maze_navigation()
else:
  create_character()
  maze_navigation()