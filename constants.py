import random


guess_count = 0
guessed_letters = []
current_menu = "MAIN"


def set_diff(diff):
    if diff == "EASY": 
        return random.randint(3, 5)
    elif diff == "MEDIUM":
        return random.randint(6, 7)
    elif diff == "HARD":
        return random.randint(8, 9)
    elif diff == "RANDOM":
        return random.randint(3, 9)
    else:
        print("Invalid Difficulty")
        return random.randint(3, 9)
    

'''words = {
    3: ['cat', 'dog', 'pig', 'bat', 'ant'],
    4: ['tree', 'bird', 'fish', 'frog', 'wolf'],
    
    5: ['apple', 'horse', 'zebra', 'tiger', 'lemon'],
    6: ['banana', 'monkey', 'orange', 'rabbit', 'pepper'],
    
    7: ['giraffe', 'pumpkin', 'dolphin', 'tornado', 'octopus'],
    8: ['elephant', 'pineapple', 'dinosaur', 'sandwich', 'bluebird'],
    9: ['kangaroo', 'alligator', 'butterfly', 'hurricane', 'porcupine'] 
}
'''

animals = {
    3: ['cat', 'dog', 'pig'],
    4: ['bird', 'fish', 'frog'],
    
    5: ['horse', 'zebra', 'tiger'],
    6: ['monkey', 'rabbit', 'donkey'],
    
    7: ['giraffe', 'dolphin', 'octopus'],
    8: ['elephant', 'bluebird', 'chipmunk'],
    9: ['kangaroo', 'alligator', 'butterfly'] 
}

countries = {
    3: ['USA', 'UAE', 'Cuba'],  
    4: ['Peru', 'Iran', 'Iraq'],  
    
    5: ['India', 'Chile', 'Japan'],  
    6: ['France', 'Brazil', 'Mexico'],  
    
    7: ['Germany', 'Hungary', 'England'],  
    8: ['Portugal', 'Thailand', 'Malaysia'],  
    9: ['Argentina', 'Indonesia', 'Colombia']
}

movies = {
    3: ['Jaws', 'It', 'Her'],  
    4: ['Dune', 'Soul', 'Nope'],  
    
    5: ['Shrek', 'Coco', 'Alien'],  
    6: ['Frozen', 'Avatar', 'Rocky'],  
    
    7: ['Titanic', 'Skyfall', 'Twister'],  
    8: ['Inception', 'Parasite', 'Gladiator'],  
    9: ['Interstellar', 'TheGodfather', 'TheNotebook']
}

fruits = {
    3: ['fig', 'pea', 'nut'],  
    4: ['pear', 'kiwi', 'plum'],  
    
    5: ['apple', 'mango', 'guava'],  
    6: ['banana', 'papaya', 'grapes'],  
    
    7: ['avocado', 'pumpkin', 'peaches'],  
    8: ['blueberry', 'pineapple', 'cucumber'],  
    9: ['strawberry', 'watermelon', 'honeyberry']
}

hangman = {  
    6: ['''     +---+\n     O   |  \n    /|\  |\n    / \  |\n        ===  '''],
    5: ['''     +---+\n     O   |  \n    /|\  |\n    /    |\n        ===  '''],
    4: ['''     +---+\n     O   |  \n    /|\  |\n         |\n        ===  '''],
    3: ['''     +---+\n     O   |  \n    /|   |\n         |\n        ===  '''],
    2: ['''     +---+\n     O   |  \n     |   |\n         |\n        ===  '''],
    1: ['''     +---+\n     O   |  \n         |\n         |\n        ===  '''],
    0: ['''     +---+\n         |  \n         |\n         |\n        ===  ''']
}

welcome_message = '''
Welcome to Hangman
By: Fantonos

1.) Start
2.) Options
3.) Quit
'''

word_cat_list = [animals, countries, movies, fruits]
dict_cat_list = ["animals", "countries", "movies", "fruits"]
word_cat_list_message = f"\nCurrently Selected Categories: {", ".join(dict_cat_list)}\nSelect a word category to add/remove:\n 1.)Animals\n 2.)Countries\n 3.)Movies\n 4.)Fruits\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"

sentence_Mode = "Off"
sentence_Mode_message = "\nSelect a sentence mode:\n 1.)On\n 2.)Off\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"

timer = "Off"
timer_message = "\nSelect a timer:\n 1.)On\n 2.)Off\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"

difficulty_message = "\nSelect a difficulty:\n 1.)Easy:\n 2.)Medium:\n 3.)Hard:\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"
difficulty = "RANDOM"

options_message = '''
1.) Difficulty:  Easy, Medium, Hard
2.) Word Categories: Animals, Countries, Movies, Fruits
3.) Sentence Mode: On or Off
4.) Timer: On or Off

M.)<-Return To Main Menu:
'''
