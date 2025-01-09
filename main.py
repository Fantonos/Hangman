import random
import threading
import time
import constants
import sys

user_input = "NONE"
stop_event = threading.Event()

def main():
    #Main game loop that directs flow based on the current menu state.

    global user_input
    
    while True:
        if user_input.upper() == "NONE":
            #Prompt user if user_input is not set
            user_input = input(f"{constants.welcome_message}\nType an option: ")
            
        if constants.current_menu == "MAIN":
            handle_main_menu()

        elif constants.current_menu == "OPTIONS":
            handle_options_menu()

        elif constants.current_menu == "GAME":
            handle_game_menu()

        else:
            #Fallback or error handling (not strictly necessary)
            print("Error: Unknown menu state. Exiting.")
            stop_event.set()
            sys.exit(0)


def handle_main_menu():
    #Handle the main menu: START, OPTIONS, QUIT, etc.
    global user_input
    global word
    global split_word
    global unsolved_word

    while constants.current_menu == "MAIN":
        #Prompt if user_input is NONE or invalid
        if user_input.upper() == "NONE":
            user_input = input(constants.welcome_message + "\nType an option: ")

        choice = user_input.upper()

        if choice in ("START", "S", "1"):
            word, split_word, unsolved_word = gen_word()
            constants.current_menu = "GAME"

        elif choice in ("OPTIONS", "O", "2"):
            constants.current_menu = "OPTIONS"
            #Reset user_input so the Options menu can prompt
            user_input = input(constants.options_message + "\nType an option: ")

        elif choice in ("QUIT", "Q", "3"):
            print("Goodbye!")
            stop_event.set()
            sys.exit(0)

        else:
            #Invalid input => re-prompt
            user_input = input(
                constants.welcome_message
                + f"\n--- '{choice}' Invalid input --- \nType an option: "
            )


def handle_options_menu():
    #Handle the 'OPTIONS' menu and sends to the sub-menus:
    global user_input

    while constants.current_menu == "OPTIONS":
        choice = user_input.upper()

        if choice in ("DIFFICULTY", "1"):
            handle_difficulty_option()

        elif choice in ("WORD CATEGORIES", "2"):
            handle_word_categories_option()

        elif choice in ("SENTENCE MODE", "3"):
            handle_sentence_mode_option()

        elif choice in ("TIMER", "4"):
            handle_timer_option()
            
        elif check_return_to_menu(choice):
            user_input = input("Type an option: ")
            break

        #Invalid input => re-prompt
        else:
            user_input = input(
                constants.options_message
                + f"\n--- '{choice}' Invalid input --- \nType an option: "
            )


def handle_difficulty_option():
    #Change difficulty: EASY, MEDIUM, HARD, RANDOM
    
    global user_input

    user_input = "NONE"
    while True:
        print(constants.difficulty_message)
        choice = user_input.upper()

        if choice in ("EASY", "1"):
            constants.difficulty = "EASY"
            print("--- Easy Mode selected ---")

        elif choice in ("MEDIUM", "2"):
            constants.difficulty = "MEDIUM"
            print("--- Medium Mode selected ---")

        elif choice in ("HARD", "3"):
            constants.difficulty = "HARD"
            print("--- Hard Mode selected ---")

        elif choice in ("RANDOM", "4"):
            constants.difficulty = "RANDOM"
            print("--- Random Mode selected ---")

        elif check_return_to_menu(choice):
            user_input = input("Type an option: ")
            break

        elif choice != "NONE":  #4 Invalid input
            print(f"--- '{choice}' Invalid input ---")

        user_input = input("Type an option: ")


def handle_word_categories_option():
    #Toggle word categories (ANIMALS, COUNTRIES, MOVIES, FRUITS).
    
    global user_input

    user_input = "NONE"
    while True:
        print(constants.word_cat_list_message)
        choice = user_input.upper()

        if choice in ("ANIMALS", "1"):
            toggle_category(constants.animals, "animals")

        elif choice in ("COUNTRIES", "2"):
            toggle_category(constants.countries, "countries")

        elif choice in ("MOVIES", "3"):
            toggle_category(constants.movies, "movies")

        elif choice in ("FRUITS", "4"):
            toggle_category(constants.fruits, "fruits")

        elif check_return_to_menu(choice):
            user_input = input("Type an option: ")
            break

        elif choice != "NONE":  #4 Invalid
            print(f"--- '{choice}' Invalid input ---")

        #Ensure at least one category is always selected
        if len(constants.dict_cat_list) == 0:
            print("\nAlert! - No categories selected, setting items to default!\n")
            constants.word_cat_list = [
                constants.animals,
                constants.countries,
                constants.movies,
                constants.fruits,
            ]
            constants.dict_cat_list = ["animals", "countries", "movies", "fruits"]

        user_input = input(
            f"Currently Selected Categories: {', '.join(constants.dict_cat_list)}\n"
            "Type an option: "
        )


def handle_sentence_mode_option():
    #Toggle sentence mode: ON or OFF
    
    global user_input

    user_input = "NONE"
    while True:
        print(constants.sentence_Mode_message)
        choice = user_input.upper()

        if choice in ("ON", "1"):
            constants.sentence_Mode = "On"
            constants.item_type = "sentence"
            print("--- Sentence Mode On ---")

        elif choice in ("OFF", "2"):
            constants.sentence_Mode = "Off"
            constants.item_type = "word"
            print("--- Sentence Mode Off ---")

        elif check_return_to_menu(choice):
            user_input = input("Type an option: ")
            break

        elif choice != "NONE":
            print(f"--- '{choice}' Invalid input ---")

        user_input = input("Type an option: ")


def handle_timer_option():
    #Toggle timer: ON or OFF
    
    global user_input

    user_input = "NONE"
    while True:
        print(constants.timer_message)
        choice = user_input.upper()

        if choice in ("ON", "1"):
            constants.timer = "On"
            print("--- Timer On ---")

        elif choice in ("OFF", "2"):
            constants.timer = "Off"
            print("--- Timer Off ---")

        elif check_return_to_menu(choice):
            user_input = input("Type an option: ")
            break

        elif choice != "NONE":
            print(f"--- '{choice}' Invalid input ---")

        user_input = input("Type an option: ")


def toggle_category(category_list, category_name):    
    #Helper function to add/remove a category (like animals, countries, etc.) from the currently selected list.

    if category_list not in constants.word_cat_list:
        constants.word_cat_list.append(category_list)
        constants.dict_cat_list.append(category_name)
        print(f"--- {category_name.capitalize()} Selected ---")
    else:
        constants.word_cat_list.remove(category_list)
        constants.dict_cat_list.remove(category_name)
        print(f"--- {category_name.capitalize()} Removed ---")


def handle_game_menu():
    #Presumably, this is where you'd handle the actual game logic.
    
    global user_input
    
    user_input = input("Guess a letter: ")
    
    #user_input, split_word, unsolved_word, word were genorated when the "Game" menu was selected
    if check_word(user_input, split_word, unsolved_word, word):
        user_input = "NONE"
        user_input = input(constants.welcome_message + "\nType an option: ")
    if user_input.upper() == "QUIT" or user_input.upper() == "Q":
        print("Goodbye!")
        stop_event.set()
        exit()


def gen_word():
    #Generate a random word, prepare split and unsolved versions,

    def print_game_state(unsolved):
        #Print information about the current game state.
        
        incorrect_guesses = ", ".join(constants.guessed_letters)
        hangman_art = constants.hangman[0][0]

        if constants.timer == "On":
            time_remaining = constants.timer_time - constants.elapsed_time
            print(
                f"{hangman_art}\n"
                f"Incorrect guess's: {incorrect_guesses}\n"
                f"Time Remaining: {time_remaining}s\n"
                f"The {constants.item_type}: {''.join(unsolved)}\n"
            )
        else:
            print(
                f"{hangman_art}\n"
                f"Incorrect guess's: {incorrect_guesses}\n"
                f"The {constants.item_type}: {''.join(unsolved)}\n"
            )

    #Get a random word from the appropriate list
    word = (random.choice(constants.word_cat_list))[
        constants.set_diff(constants.difficulty)
    ][random.randint(0, 2)]  #Good luck trying to understand this T-T
    
    split_word = list(word.lower())
    unsolved_word = ["_" for _ in split_word]

    #Handle special cases (sentence mode or specific words)
    if constants.sentence_Mode == "On" or word == "The Notebook" or word == "The God father":
        check_word(" ", split_word, unsolved_word, word)
    else:
        print_game_state(unsolved_word)

    #This is for the timer!
    if constants.timer == "On":
        timer_thread = threading.Thread(target=timer, args=(constants.timer_time, stop_event))
        timer_thread.start()

    return word, split_word, unsolved_word
      
      
def check_word(user_input, split_word, unsolved_word, word):
    #Check if the user input is correct or not.
    
    if check_if_win(unsolved_word, split_word, user_input, word):
        return True
    
    if user_input in split_word and constants.guess_count < 6:
        for i in range(len(split_word)):
            if split_word[i] == user_input:
                unsolved_word[i] = user_input
    else:
        constants.guess_count += 1
        constants.guessed_letters.append(user_input)
        if constants.guess_count >= 6:
            print(constants.hangman[constants.guess_count][0])
            print(f'You Lost! :(\nThe {constants.item_type} was: "{word}" \n')
            reset_game()
            return True
    
    if check_if_win(unsolved_word, split_word, user_input, word):
        return True
    
    print(constants.hangman[constants.guess_count][0])
    print(f"Incorrect guess's: {", ".join(constants.guessed_letters)}")
    if constants.timer == "On":
        print(f'Time Remaining: {constants.timer_time - constants.elapsed_time}s\nThe {constants.item_type}: {"".join(unsolved_word)}\n')
    else:
        print(f'\nThe {constants.item_type}: {"".join(unsolved_word)}\n')


def reset_game():
    #reset the game state
    stop_event.set()
    
    constants.current_menu = "MAIN"
    constants.guess_count = 0
    constants.elapsed_time = 0
    constants.guessed_letters = []
    
    input("*Press enter to continue*")
    print(constants.welcome_message)
    
    #Clear the stop event on the timer, allows the timer to be restarted
    stop_event.clear()


def check_return_to_menu(user_input):
    #Create a mapping of commands to actions
    menu_commands = {
        "RETURN TO OPTIONS": ("OPTIONS", constants.options_message),
        "O": ("OPTIONS", constants.options_message),
        "RETURN TO MENU": ("MAIN", constants.welcome_message),
        "M": ("MAIN", constants.welcome_message),
    }

    #Normalize user input for case-insensitive matching
    command = user_input.upper()

    #Handle menu navigation commands
    if command in menu_commands:
        constants.current_menu, message = menu_commands[command]
        print(message)
        return True

    #Handle quit command
    if command in {"QUIT", "Q"}:
        print("Goodbye!")
        stop_event.set()
        exit()

    return False

 
def check_if_win(unsolved_word, split_word, user_input, word):
    is_word_solved = unsolved_word == split_word
    is_guess_correct = user_input.upper() == word.upper()
    can_still_guess = constants.guess_count < 6

    if (is_word_solved or is_guess_correct) and can_still_guess:
        print(
            f"{constants.hangman[constants.guess_count][0]}\n"
            f"You win!\n\n"
            f"That's Correct! The {constants.item_type} was: '{word}'.\n"
        )
        reset_game()
        return True

    return False


def timer(seconds, stop_event):
    constants.elapsed_time = 0
    interval = 0.25  #Check the stop event and increment elapsed time at this interval

    while constants.elapsed_time < seconds:
        if stop_event.is_set():  #Stop the timer if the event is set (User lost or  won)
            return
        time.sleep(interval)
        constants.elapsed_time += interval

    print("\nTime's Up!\n*Press enter to continue*")
    constants.guess_count = 6  #set guess count to 6 to end the game
    
    
stop_event = threading.Event()

main()

