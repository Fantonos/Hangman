# Hangman
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

A simple terminal-based Hangman game written in Python 3. This game includes multiple features such as difficulty levels, various word categories, an optional sentence mode, and an optional timer.

---

## Features

1. **Main Menu**  
   - Start the game  
   - Go to Options  
   - Quit

2. **Options Menu**  
   - **Difficulty**: Easy, Medium, Hard, or Random  
   - **Word Categories**: Animals, Countries, Movies, Fruits  
   - **Sentence Mode**: Toggle On/Off (guesses sentences instead of single words)  
   - **Timer**: Toggle On/Off  

3. **Game Flow**  
   - Randomly picks a word (or sentence) based on the selected categories and difficulty.  
   - Tracks incorrect guesses with a simplistic Hangman ASCII art.  
   - Allows you to win by guessing all letters or lose by reaching 6 incorrect guesses (or running out of time if the timer is on).

4. **Timer** (optional)  
   - Counts down the time you have to guess.  
   - If time runs out, the game ends.  

5. **Multiple Word Categories**  
   - You can enable or disable different categories (animals, countries, movies, fruits) at will.

---

## Requirements

- Python 3.x  
- [constants.py](#constants-py-details) located in the same directory as the main script.  

No external libraries are required. This game does not rely on any additional data files, just the two `.py` files.

---

## Installation & Setup

1. **Clone or download the repository**  
   ```bash
   git clone https://github.com/your-username/hangman-game.git
   ```
2. **Navigate to the project folder**
   ```bash
   cd hangman
   ```

3. **Ensure constants.py is in the same folder**
   Make sure the main script and constants.py are both in the same directory.

4. **(Optional) Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Run the game**
   ```bash
   python main_script.py
   ```

## Usage

### Start the Game
- On launching, you will see a welcome message. Type ``START`` (or ``S`` or ``1``) to begin a new Hangman game.
- Alternatively, navigate to ``OPTIONS`` (or ``O`` or ``2``) to configure settings before starting.

### Options Menu
- **Difficulty**:  
  - ``1`` for Easy  
  - ``2`` for Medium  
  - ``3`` for Hard  
  - ``4`` for Random  

- **Word Categories**: Toggle categories on or off. You can keep multiple categories active at once.
- **Sentence Mode**: Turn it on (``ON``/``1``) to guess sentences, or off (``OFF``/``2``) to guess single words.
- **Timer**: Turn it on (``ON``/``1``) or off (``OFF``/``2``). If the timer is on, it begins counting down as soon as the game starts.

### Gameplay
- Enter your guess when prompted:
  - A single letter (e.g., ``A``)
  - Or, if you think you know the entire word or sentence, try typing it in full.
- You lose after **6** incorrect guesses.
- If using the timer and it runs out, you also lose the game.

### Exiting
- Type ``QUIT`` (or ``Q``) whenever prompted to exit the game.


## License

This project is open-source and available under the MIT License.

[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)