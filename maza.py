
# Name: Jerrod Bolton
# Date: Nov 20,2025
# Python class 235 Programming I - Assignment Function and Loops
# For the assignment, I'll be adding functions and loops to my maze game. this is so that the # gamer don't have to start over every time they make a wrong move.

# I would like to make a program that simulates a simple Maze game. Where a people can navigate through a maze using text commands.


# character_detail = []

def  maze_navigation(): 
    # Maze navigation simulation
    # the correct answers to get through the maze are south, west, east, north.

    print("You are in round one of the maze. You can move north, south, east, or west.")
    print("Type 'exit' to leave the maze.")
    start = input("Would you like to start the game (yes/no): ").lower()

    if start == 'yes' or start == 'y':
        directions = input("What directions would like to go? (north/south/east/west): ").lower()
    # this is the first round that the user will play through.
        if directions == 'north':
            print("You moved north and found a dead end. Try again!")
        elif directions == 'south':
            # this is  the first round that the user will play through.
            print("You moved south and move to round two!")
            print("=======================================================")
            print("Round 1 complete! Starting round 2...")
            # this is the second round that the user will play through.
            directions = input("What directions would like to go? (north/south/east/west): ").lower()
            while directions != "west":
         
                print("You moved west and move to round three!")
                print("=======================================================")
                print("Congratulations on completed round two!")
                print("=======================================================")
                print("Starting Round 3... GET READY!")
                # this is the third round that the user will play through.
                directions = input("What directions would like to go? (north/south/east/west): ").lower()
                if directions == 'north':
                    print("You moved north and found a dead end. Try again!")
                elif directions == 'south':
                    print("You moved south and found a dead end. Try again!")
                elif directions == 'east':
                    print("You moved east and move to round four!")
                    print("=======================================================")
                    print("Congratulations on completed round three!")
                    print("=======================================================")
                    print("Starting Round 4... Ready or NOT!")
                # this is the third round that the user will play through.
                    directions = input("What directions would like to go? (north/south/east/west): ").lower()
                    if directions == 'north':
                        print("You moved north and found yourself back at the started in the maze. Exactly where you need to be! Live large! Be happy, and play again if you need.")
                    elif directions == 'south':
                        print("You moved south and found a dead end. Try again!")
                    elif directions == 'east':
                        print("You moved east and found a dead end. Try again!")
                    elif directions == 'west':
                        print("You moved west and found a dead end. Try again!")
                    else:
                        print("You would like to exit the maze. Goodbye!")
                elif directions == 'west':
                    print("You moved west and found a dead end. Try again!")
                else:
                    print("You would like to exit the maze. Goodbye!")
            else:
                print("You would like to exit the maze. Goodbye!")
            
        elif directions == 'east':
            print("You moved east and encountered a monster! Game over!")
        elif directions == 'west':
            print("You moved west and found a dead end. Try again!")
        else:
            print("You would like to exit the maze. Goodbye!")
    else:
        print("Maybe next time! Goodbye!")


    
def create_character():  
    
    # i also would lie to save the character details to a text file. 
    # Saving the character by name went a person is playing. 

    save_character = input("Would you like to save your character? (yes/no): ")
    if save_character == 'yes' or save_character == 'y':    
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
            

    
        # character_detail.append(character_name)
        # character_detail.append(character_design)
        # character_detail.append(character_origin)
        # character_detail.append(character_eye_color)
        # character_detail.append(character_hair_color)
        # character_detail.append(character_age)


    

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
  maze_navigation()
else:
  create_character()
  maze_navigation()