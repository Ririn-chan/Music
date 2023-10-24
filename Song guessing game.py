#!/usr/bin/env python

#playsound(r'C:\\Users\\PSC\Downloads\\ES Starlight Parade - fine & Knights KANROMENGIND.mp3')
#playsound(r')
import random
from playsound import playsound
#playsound(r'C:\\Users\\PSC\Downloads\\ES Starlight Parade - fine & Knights KANROMENGIND.mp3')
def main():
    """"Start a enstars song guessing game."""
    print("Guess the song! ")

    hint=[
       "Starlight parade by fine & knights",
       "Twillight Pentagram by altered",
       "Believe 4 leaves by alkaloid",
       "Ryusei Hanabi by ryuseitai",
    ] 

    x=random.choice(hint)
    print(x) 
    guess=None

    while x!=guess:

    from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav('Music1.wav')
play(song)

      guess=str(input ("what enstars song am i played?"))
      if x== guess:
        print("You guessed {}. Congratulations,you got it right!" .format (guess))
        playsound('C:\\Users\\PSC\\Music\\song\\1.mp3')
        break
      else:

        print("You guessed {}. Unfortunately you got the wrong answer. Please try again." .format (guess))


main()