# SquidGame
Python implementation of some Squid Games.
This is a poor man's version of Red light-green light from Squid Game.
The correct translation of the game is actually "Mugunghwa (national flower of Korea)
flowers blossomed." The rule is also slightly different.
In red light-green light, "it" holds up either a green or red signal to control the players' movements.
In Mugunghwa game, the players are free to move while the "it" turns around and recite
"Mugunghwa flowers blossomed." After reciting is done, "it" faces the players and detects if anyone is moving.
If anyone moves during this time, he/she is eliminated (killed in the movie).

This version of the game is safe because it mimics the game in Python 
without killing the players.


# Setup
1. Install
- pip install opencv-python
- pip install yolov5
- pip install playsound
