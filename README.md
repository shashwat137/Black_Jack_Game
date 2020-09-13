[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)  

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)
# Black_Jack_Game
Black Jack game in Python between a player and computer.
The computer acts as the dealer while player can bet on games.
Player may choose his/her initial pot amount and may bet on each round on an amount of their choice. Chips are added or removed from the pot as the game progresses depending on the outcome. The player may exit the game at the end of any round. The game will end if the player has no more chips available in the pot.
The Dealer will hit until he reaches a score of 17. If he reaches a value greater than 17, he will stand irrespective of whether the player has reached a higher amount or not (Unless the dealer busts).
For now only 'Hit' and 'Stand' functionality is included. 'Split', 'Double Down' and 'Surrender' options are not supported as of now.

## Getting Started
Download the whole repository and save it to a folder on your PC. Make sure you have pre requisites installed. Run the [blackjack.py](blackjack.py) and the game will start.

### Prerequisites
Things you need to install.
```
Python 3
```
Alternatively, you may also use (optional)
```
Jupyter Notebook
Anaconda Prompt
```

### Running the Program
Go to the location of the [blackjack.py](blackjack.py) on the command line. To run it enter the following.
On Windows:
```
python blackjack.py
```
On Linux/Mac:
```
python3 blackjack.py
```
Alternatively, you may run the program on Jupyter Notebook. Open Anaconda Prompt and move to the directory where the [blackjack.py](blackjack.py) is stored. Enter the following in Anaconda Prompt.
```
jupyter notebook
```
A Jupyter Notebook will open. Open a Python3 notebook. Enter the following command in the cell and press Shift+Enter
```
import blackjack
```
Follow the onscreen instructions and play.

### Built with
* Python

### Author
* Shashwat

### Acknowledgements
* Link to the Tutorial from which the game was made - [Complete Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/)
* I made this as a personal project to learn and have fun. Incorporated OOP in Python to get a better command of OOP.
