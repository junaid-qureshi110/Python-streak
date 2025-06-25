import random
import os
import pyttsx3
import pyjokes
import sys

# Jokes module--------------
# import pyjokes
print(sys.version)
joke = pyjokes.get_joke()Q 
print("jokes---->",joke)

# Q. install an external module and use it to perform an operation of your interest?
#Text To Speech ----------------------
# import pyttsx3 
engine = pyttsx3.init()
# engine.say("I will speak this text")
engine.say("Hello JUNAID sir")
engine.runAndWait()

# Q. WAP to print the contents of a directory using the os module,Search online for the function which does that?----------------

# import os
# specify the directory you want to list
directory_path = "/my resume"

# get and print the contents of the directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
 

# Import the random module, and display a random number from 1 to 9:-------------------

# import random
print("random number ----->",random.randrange(1, 10))
