import random
import threading
import time
import constants


def main():
    user_input = input(constants.welcome_message + "\nType an option: ")
    
    while True:
        while constants.current_menu == "MAIN":
            if user_input.upper() == "START" or user_input == "1" or user_input.upper() == "S":
                word, split_word, unsolved_word = gen_word()
                constants.current_menu = "GAME"
                
            elif user_input.upper() == "OPTIONS" or user_input == "2" or user_input.upper() == "O":
                #print(constants.options_message)
                constants.current_menu = "OPTIONS"
                user_input = input(constants.options_message + f"\nType an option: ")
                
            elif user_input.upper() == "QUIT" or user_input == "3" or user_input.upper() == "Q":
                    print("Goodbye!")
                    stop_event.set()
                    exit() 
            elif user_input.upper() != "NONE":
                user_input = input(constants.welcome_message + f"\n--- '{user_input.upper()}' Invalid input --- \nType an option: ")
            
        while constants.current_menu == "OPTIONS":     

            if user_input.upper() == "DIFFICULTY" or user_input == "1":
                user_input = "NONE"
                while True:
                    print(constants.difficulty_message)
                    if user_input.upper()== "EASY" or user_input == "1":
                        print(constants.difficulty_message)
                        constants.difficulty = "EASY"
                        print("--- Easy Mode selected ---")
                    elif user_input.upper()== "MEDIUM" or user_input == "2":
                        print(constants.difficulty_message)
                        constants.difficulty = "MEDIUM"
                        print("--- Medium Mode selected ---")
                    elif user_input.upper()== "HARD" or user_input == "3":
                        print(constants.difficulty_message)
                        constants.difficulty = "HARD"
                        print("--- Hard Mode selected ---")
                    elif user_input.upper()== "RANDOM" or user_input == "4":
                        print(constants.difficulty_message)
                        constants.difficulty = "RANDOM"
                        print("--- Random Mode selected ---")
                    elif user_input.upper() != "NONE":
                        print(f"--- '{user_input.upper()}' Invalid input ---")
                    if check_return_to_menu(user_input):  
                        user_input = input("Type an option: ")                
                        break
                    user_input = input("Type an option: ")
                    
            elif user_input.upper() == "WORD CATEGORIES" or user_input == "2":
                user_input = "NONE"
                while True:
                    print(constants.word_cat_list_message)
                    if user_input.upper()== "ANIMALS" or user_input == "1":
                        if constants.animals not in constants.word_cat_list:
                            constants.word_cat_list.append(constants.animals)
                            constants.dict_cat_list.append("animals")
                            print("--- Animals selected ---")
                        else:
                            constants.word_cat_list.remove(constants.animals)
                            constants.dict_cat_list.remove("animals")
                            print("--- Animals Removed ---")
                            
                    elif user_input.upper()== "COUNTRIES" or user_input == "2":
                        if constants.countries not in constants.word_cat_list:
                            constants.word_cat_list.append(constants.countries)
                            constants.dict_cat_list.append("countries")
                            print("--- Countries Selected ---")
                        else:
                            constants.word_cat_list.remove(constants.countries)
                            constants.dict_cat_list.remove("countries")
                            print("--- Countries Removed ---")

                    elif user_input.upper()== "MOVIES" or user_input == "3":
                        if constants.movies not in constants.word_cat_list:
                            constants.word_cat_list.append(constants.movies)
                            constants.dict_cat_list.append("movies")
                            print("--- Movies Selected ---")
                        else:
                            constants.word_cat_list.remove(constants.movies)
                            constants.dict_cat_list.remove("movies")
                            print("--- Movies Removed ---")

                    elif user_input.upper()== "FRUITS" or user_input == "4":
                        if constants.fruits not in constants.word_cat_list:
                            constants.word_cat_list.append(constants.fruits)
                            constants.dict_cat_list.append("fruits")
                            print("--- Fruits Selected ---")
                        else:
                            constants.word_cat_list.remove(constants.fruits)
                            constants.dict_cat_list.remove("fruits")
                            print("--- Fruits Removed ---")
                    elif check_return_to_menu(user_input):  
                        user_input = input("Type an option: ")                
                        break
                    elif user_input.upper() != "NONE":
                        print(f"--- '{user_input.upper()}' Invalid input ---")
                    
                    if check_return_to_menu(user_input):   
                        user_input = input("Type an option: ")               
                        break
                    
                    if len(constants.dict_cat_list) == 0:
                        print("\n Alert! - No categories selected, setting items to default!\n")
                        constants.word_cat_list = [constants.animals, constants.countries, constants.movies, constants.fruits]
                        constants.dict_cat_list = ["animals", "countries", "movies", "fruits"]
                        
                    user_input = input(f"Curently Selected Categories: {', '.join(constants.dict_cat_list)}\n Type an option: ")

            elif user_input.upper() == "SENTENCE MODE" or user_input == "3":
                user_input = "NONE"
                while True:
                    print(constants.sentence_Mode_message)
                    if user_input.upper()== "ON" or user_input == "1":
                        print(constants.sentence_Mode_message)
                        constants.sentence_Mode = "On"
                        constants.item_type = "sentence"
                        print("--- Sentence Mode On ---")
                        
                    elif user_input.upper()== "OFF" or user_input == "2":
                        print(constants.sentence_Mode_message)
                        constants.sentence_Mode = "Off"
                        constants.item_type = "word"
                        print("--- Sentence Mode Off ---")
                        
                    elif check_return_to_menu(user_input):
                        user_input = input("Type an option: ")
                        break
                    
                    elif user_input.upper() != "NONE":
                        print(f"--- '{user_input.upper()}' Invalid input ---")

                    user_input = input("Type an option: ")

            elif user_input.upper() == "TIMER" or user_input == "4":
                user_input = "NONE"
                while True:
                    print(constants.timer_message)
                    if user_input.upper()== "ON" or user_input == "1":
                        print(constants.timer_message)
                        constants.timer = "On"
                        print("--- Timer On ---")

                    elif user_input.upper()== "OFF" or user_input == "2":
                        print(constants.timer_message)
                        constants.timer = "Off"
                        print("--- Timer Off ---")

                    elif check_return_to_menu(user_input):
                        user_input = input("Type an option: ")
                        break

                    elif user_input.upper() != "NONE":
                        print(f"--- '{user_input.upper()}' Invalid input ---")
                    
                    user_input = input("Type an option: ")

            elif check_return_to_menu(user_input):
                user_input = input("Type an option: ")
                break  
            else:
                user_input = input(constants.options_message + f"\n--- '{user_input.upper()}' Invalid input --- \nType an option: ")

          
        while constants.current_menu == "GAME":
            user_input = input("Guess a letter: ")
            if check_word(user_input, split_word, unsolved_word, word):
                user_input = "NONE"
                user_input = input(constants.welcome_message + "\nType an option: ")
                break
            if user_input.upper() == "QUIT" or user_input.upper() == "Q":
                print("Goodbye!")
                stop_event.set()
                exit()


def gen_word():
        word = (random.choice(constants.word_cat_list))[constants.set_diff(constants.difficulty)][random.randint(0, 2)] #Good luck, trying to under this
        split_word = list(word.lower())
        unsolved_word = list("_" * (len(word.lower())))

        if constants.sentence_Mode == "On":
            check_word(" ", split_word, unsolved_word, word)    
        else:
            if constants.timer == "On":
                print(f"{constants.hangman[0][0]}\nIncorrect guess's: {", ".join(constants.guessed_letters)}\nTime Remaining: {constants.timer_time - constants.elapsed_time}s\nThe {constants.item_type}: {''.join(unsolved_word)}\n")
            else:
                print(f"{constants.hangman[0][0]}\nIncorrect guess's: {", ".join(constants.guessed_letters)}\nThe {constants.item_type}: {''.join(unsolved_word)}\n")
        if constants.timer == "On":
            timer_thread = threading.Thread(target=timer, args=(constants.timer_time, stop_event))
            timer_thread.start()
        return word, split_word, unsolved_word
      
def check_word(user_input, split_word, unsolved_word, word):
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
    stop_event.set()
    constants.current_menu = "MAIN"
    input("*Press enter to continue*")
    print(constants.welcome_message)
    constants.guess_count = 0
    constants.elapsed_time = 0
    constants.guessed_letters = []
    stop_event.clear()
    return
    
def check_return_to_menu(user_input):
    if user_input.upper() == "RETURN TO OPTIONS" or user_input.upper() == "O":
        constants.current_menu = "OPTIONS"
        print(constants.options_message)
        return True
    elif user_input.upper() == "RETURN TO MENU" or user_input.upper() == "M":
        constants.current_menu = "MAIN"
        print(constants.welcome_message)
        return True
    
    elif user_input.upper() == "QUIT" or user_input.upper() == "Q":
        print("Goodbye!")
        stop_event.set()
        exit()
    return False
    
def check_if_win(unsolved_word, split_word, user_input, word):
        if (unsolved_word == split_word or user_input.upper() == word.upper()) and constants.guess_count < 6:
            print(f"{constants.hangman[constants.guess_count][0]}\nYou win!\n\nThat's Correct! The {constants.item_type} was: '{word}'.\n")
            reset_game()
            return True
        return False  

def timer(seconds, stop_event):
    constants.elapsed_time = 0
    while constants.elapsed_time < seconds:
        if stop_event.is_set():  # Check if the stop signal is set
            return
        time.sleep(.25)
        constants.elapsed_time += .25 
    print("\nTimes Up!\n*Press enter to continue*")
    constants.guess_count = 6
    
stop_event = threading.Event()

main()

