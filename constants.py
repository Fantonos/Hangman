import random


guess_count = 0
guessed_letters = []
current_menu = "MAIN"
global timer_time

def set_diff(diff):
    global timer_time
    if sentence_Mode == "On":
        sentence_multiplier = 10
    else:
        sentence_multiplier = 0
    
    if diff == "EASY": 
        timer_time = 60
        return random.randint(3 + sentence_multiplier, 5 + sentence_multiplier)
    elif diff == "MEDIUM":
        timer_time = 45
        return random.randint(6 + sentence_multiplier, 7 + sentence_multiplier)
    elif diff == "HARD":
        timer_time = 30
        return random.randint(8 + sentence_multiplier, 9 + sentence_multiplier)
    elif diff == "RANDOM":
        timer_time = random.randint(30, 60)
        return random.randint(3 + sentence_multiplier, 9 + sentence_multiplier)
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
    9: ['kangaroo', 'alligator', 'butterfly'],
    
    13: ["The dog barked loudly", "A cat chased a mouse", "I love my pet rabbit"],
    14: ["The lion roars at night", "Birds fly in the sky", "A fish swims in water"],
   
    15: ["The tiger stalks its prey in the jungle", "The elephant has big ears", "A giraffe eats leaves from tall trees"],
    16: ["The horse galloped across the field", "The kangaroo jumped over the fence", "The monkey swung from tree to tree"],
   
    17: ["The octopus hides in the coral reef", "The cheetah chased the gazelle across the savanna", "A walrus hauls itself onto the icy shore"],
    18: ["The rhinoceros charges through the grassy plain", "The flamingo stands on one leg in the swamp", "A platypus swims gracefully in the river"],
    19: ["The wolf howls at the full moon", "The squirrel climbed the tall oak tree", "The zebra blends into the grassy plains"]

}

countries = {
    3: ['USA', 'UAE', 'Cuba'],  
    4: ['Peru', 'Iran', 'Iraq'],  
    
    5: ['India', 'Chile', 'Japan'],  
    6: ['France', 'Brazil', 'Mexico'],  
    
    7: ['Germany', 'Hungary', 'England'],  
    8: ['Portugal', 'Thailand', 'Malaysia'],  
    9: ['Argentina', 'Indonesia', 'Colombia'],
    
    13: ["I live in the United States", "France is famous for its Eiffel Tower", "Japan has a lot of temples"],
    14: ["Canada is cold in the winter", "Brazil is known for its rainforests", "Italy has delicious pizza"],
    
    15: ["The United Kingdom has many historic castles", "India is home to the Taj Mahal", "Australia is surrounded by the Pacific Ocean"],
    16: ["Russia is the largest country in the world", "China has the Great Wall", "Mexico is famous for its ancient pyramids"],
    
    17: ["Egypt is home to the Pyramids of Giza", "Argentina has beautiful landscapes and tango music", "Iceland experiences midnight sun in the summer"],
    18: ["Thailand is known for its stunning beaches and temples", "New Zealand is known for its dramatic landscapes", "Nepal is home to Mount Everest"],
    19: ["Italy is famous for its art and history", "Germany has beautiful castles", "Sweden is known for its natural beauty"] 
}

movies = {
    3: ['Jaws', 'It', 'Her'],  
    4: ['Dune', 'Soul', 'Nope'],  
    
    5: ['Shrek', 'Coco', 'Alien'],  
    6: ['Frozen', 'Avatar', 'Rocky'],  
    
    7: ['Titanic', 'Skyfall', 'Twister'],  
    8: ['Inception', 'Parasite', 'Gladiator'],  
    9: ['Interstellar', 'The God father', 'The Note book'],
    
    13: ["I love the movie Frozen", "The Lion King is a great film", "Star Wars is very popular"],
    14: ["Finding Nemo is a funny movie", "Toy Story is an animated classic", "The Wizard of Oz is a colorful film"],
    
    15: ["The Matrix has great action scenes", "Jurassic Park is about dinosaurs", "Harry Potter is a wizarding adventure"],
    16: ["Titanic is a tragic love story", "The Avengers fight together to save the world", "The Godfather is a famous mafia movie"],
    
    17: ["Inception explores the world of dreams", "Pulp Fiction has non-linear storytelling", "The Shawshank Redemption is about hope and freedom"],
    18: ["Interstellar explores space and time travel", "The Grand Budapest Hotel is visually stunning", "Fight Club has a surprising plot twist"],
    19: ["The Dark Knight is an intense superhero film", "The Matrix has iconic slow-motion action scenes", "The Incredibles is about a family of superheroes"]

}

fruits = {
    3: ['fig', 'pea', 'nut'],  
    4: ['pear', 'kiwi', 'plum'],  
    
    5: ['apple', 'mango', 'guava'],  
    6: ['banana', 'papaya', 'grapes'],  
    
    7: ['avocado', 'pumpkin', 'peaches'],  
    8: ['blueberry', 'pineapple', 'cucumber'],  
    9: ['strawberry', 'watermelon', 'honeyberry'],
    
    13: ["I love eating apples", "Bananas are yellow and sweet", "Oranges are very juicy"],
    14: ["Grapes are small and round", "I eat strawberries for dessert", "Pineapple has a spiky skin"],
    
    15: ["Mangoes grow in tropical regions", "Peaches have a soft and fuzzy skin", "Lemons are sour but refreshing"],
    16: ["Cherries are red and delicious", "Avocados are creamy and healthy", "Watermelons are great for summer"],
    
    17: ["Pomegranates have many small seeds inside", "Papayas are sweet and often used in smoothies", "Kiwi fruit has a green interior with tiny seeds"],
    18: ["Dragon fruit has a vibrant pink skin", "Figs are sweet and come from a small tree", "Passion fruit has a unique tangy taste"],
    19: ["Blueberries are small and sweet", "Raspberries are tart and delicious", "Cantaloupe is a sweet summer fruit"]

}

hangman = {  
    7: ['''     +---+\n    \O/  |  \n     |   |\n    /~\  |\n        ===  '''],       
    6: ['''     +---+\n     O   |  \n    /|\  |\n    / \  |\n        ===  '''],
    5: ['''     +---+\n     O   |  \n    /|\  |\n    /    |\n        ===  '''],
    4: ['''     +---+\n     O   |  \n    /|\  |\n         |\n        ===  '''],
    3: ['''     +---+\n     O   |  \n    /|   |\n         |\n        ===  '''],
    2: ['''     +---+\n     O   |  \n     |   |\n         |\n        ===  '''],
    1: ['''     +---+\n     O   |  \n         |\n         |\n        ===  '''],
    0: ['''     +---+\n         |  \n         |\n         |\n        ===  ''']
}

print(hangman[7][0])

welcome_message = '''
Welcome to Hangman
By: Fantonos

1.) Start
2.) Options
3.) Quit
'''
item_type = "word"
word_cat_list = [animals, countries, movies, fruits]
dict_cat_list = ["animals", "countries", "movies", "fruits"]
word_cat_list_message = f"\nCurrently Selected Categories: {", ".join(dict_cat_list)}\nSelect a word category to add/remove:\n 1.)Animals\n 2.)Countries\n 3.)Movies\n 4.)Fruits\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"

sentence_Mode = "Off"
sentence_Mode_message = "\nSelect a sentence mode:\n 1.)On\n 2.)Off\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"


timer = "Off"
timer_time = 60
elapsed_time = 0
timer_message = "\nSelect a timer:\n 1.)On\n 2.)Off\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"

difficulty_message = "\nSelect a difficulty:\n 1.)Easy:\n 2.)Medium:\n 3.)Hard:\n 4.)Random:\n\n O.)<-Return to Options: \n M.)<-Return To Main Menu:\n"
difficulty = "RANDOM"

options_message = '''
1.) Difficulty: Easy, Medium, Hard
2.) Word Categories: Animals, Countries, Movies, Fruits
3.) Sentence Mode: On or Off
4.) Timer: On or Off

M.)<-Return To Main Menu:
'''
