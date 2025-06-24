import os
import pyttsx3
import pyjokes
import sys
print(sys.version)
joke = pyjokes.get_joke()
print(joke)

# Q.3 install an external module and use it to perform an operation of your interest?

# import pyttsx3 
engine = pyttsx3.init()
# engine.say("I will speak this text")
engine.say("Hello JUNAID sir")
engine.runAndWait()

# Q.4 WAP to print the contents of a directory using the os module,Search online for the function which does that?


# import os
# specify the directory you want to list
directory_path = "/my resume"

# get and print the contents of the directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
 