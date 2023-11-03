#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        letter = open("./Input/Letters/starting_letter.txt")
        contents = letter.read()
        letter.close()
        contents = contents.replace(PLACEHOLDER, name.strip())
        letter = open(f"./Output/ReadyToSend/{name.strip()}.txt", "w")
        letter.write(contents)
        letter.close()


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp