import time
import os.path


#this will make sure the file exists for storage of information. If file
#doesn't exist it will create one

if (os.path.isfile("dictionary.txt")):
    pass


else:
    with open("dictionary.txt", "w+") as text_file:
                #writes {} to it so that it gets interpreted as a dictionary
                dictionary = text_file.write("{}")
                print("Couldn't find dictionary text file, so a new one was created.")

while True:
    action = input("would you like to create, delete, view data, or quit? ")
    print()
    if (action in ["create", "create data", "c"]):
            #the imported dictionary from the text file is a string and must be coverted to
            #dictionary before use. I'll use the eval function to convert the
            #string into dictionary.

        with open("dictionary.txt") as text_file:
            dictionary = text_file.readline()
        dictionary = eval(dictionary)

                    
        print("length of the dictionary is:", len(dictionary))
        print()

        #finds the ID or index of the last person in the list and adds 1 to it.
        #if no people are in the list the index number will be 0.
        try:
            new_person = list(dictionary)[-1] + 1
        except:
            new_person = 0


        #adds a tab per say to store the new persons's information.
        dictionary[new_person] = {}


        #finds the ID of the last person within the dictionary and adds 1 to it to make
        #the ID of a new person within the dictionary.

        for trait in ["name","age","gender"]:
            dictionary[new_person][trait] = str(input("what is your " + trait + "? "))
            print()

        #adds a new piece of info to every trait(name, etc...)


        for person, info in dictionary.items():
            print()
            print ("ID:", person)
            #prints person's ID
            for piece in info:
                #for every piece of info, name, gender, etc... it will print it and the corresponding information.
                #for example a piece will be name and the corresponding info will be john.
                print(piece + ":", dictionary[person][piece])
            
        #overwrites everything within the dictionary and replaces it with the
        #new dictionary
        with open("dictionary.txt", "w+") as text_file:
            dictionary = text_file.write(str(dictionary))

        print()

    #simply turns off the program.        
    elif (action in ["quit", "q"]):
        break

    #views and presents all of the people within the dictionary.
    elif (action in ["view", "view data", "v"]):

        with open("dictionary.txt") as text_file:
            dictionary = text_file.readline()
            dictionary = eval(dictionary)
            for ID, info in dictionary.items():
                print()
                print("ID:" + str(ID))
                for piece in info:
                    print(piece + ": " + info[piece])
        print()

            
    elif (action in ["delete", "delete data", "d"]):
            with open("dictionary.txt") as text_file:
                dictionary = text_file.readline()
                dictionary = eval(dictionary)
                #prevents the program from crashing if a user enters a string.
                try:
                    user_to_delete = int(input("Which user ID to delete? "))
                    #if statement makes sure the user does exist.
                    #if user doesn't exist and an edit attempt happens, file becomes
                    #blank.
                    if (user_to_delete in dictionary):
                        with open("dictionary.txt", "w+") as text_file:
                            print()
                            print(dictionary[user_to_delete])
                            del dictionary[user_to_delete]
                            text_file.write(str(dictionary))
                    else:
                        print("User doesn't exist.")
                    
                except:
                    print("invalid input")

    else:
        print("Invalid input, please enter a valid command.")
        print()
                
