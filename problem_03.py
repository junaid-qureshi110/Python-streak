# Q.1 WAP to display a user entered name followed by Good Afternoon using input() function?

name = input("Enter Your Name: ")
print("Good Afternoon "+ name)


name = input("Enter your name: ")
print(f"Good Afternoon, {name} ") 

# Q.2 WAP to fill in a letter template given below with name and date ?
# letter = '''
#        Dear <|Name|>,
#        You are selected!
#        <|Date|>
#          '''

letter = '''
       Dear <|Name|>,
       You are selected!
       <|Date|>
         '''
print(letter.replace("<|Name|>","Junaid").replace("<|Date|>","25 June 2025"))

# Q.3 WAP to detect double space in a string?
name = "Junaid is a good  boy and  "

print(name.find("  "))
print(name) # Strings are immutable which means that you cannot change them by running functions on them. 