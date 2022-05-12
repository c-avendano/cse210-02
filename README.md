# Hilo
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 hilo 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- hilo                (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Cristian Avendano, Shanny Serrano, Kelley Robertson



-------------------------


------------------------

class: Leader

(this is like the "main" function on python)

"""Ensure the following:

The player starts the game with 300 points.
display class Deck.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over."""



- high_or_low: user chooses wheter the next card is higher or lower, based on result it affects the points
# shanny

- Points: you start with 300 -- should add or remove points based on high_or_low result. 0 means game over. After calculation from "Current card", if result isn't 0 ask the user if they want to keep playing.
# for cristian

- Current card: the value we get from Deck, then it calculates if it's higher or lower than the previous value
# kelley


--------------------------------

class: Deck

"generates random number between 1-13"


--------------------------------