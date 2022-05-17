import time
while True:
    action = input("would you like to create, delete, view data, or quit? ")
    if (action == "create" or action == "c"):
        try:
            with open("dictionary.txt") as Reader:
                dictionary = Reader.readline()
        except:
            with open("dictionary.txt", "w+") as Reader:
                dictionary = Reader.write("{}")

            #the imported dictionary from the text file is a string and must be coverted to
            #dictionary before use. I'll use the eval function to convert the
            #string into dictionary.
        try:
            dictionary = eval(dictionary)
        except:
            print()
            print("Couldn't find dictionary text file, so a new one was created.")
            
        dictionary_of_names = dictionary
        print()

            #please excuse the following horrible lines of code.
        
        try:
            print("length of the dictionary is:", len(dictionary_of_names))
            print()
            
        except:
            print("length of the dictionary is: 0")

        try:
            new_person = list(dictionary_of_names)[-1] + 1
        except:
            new_person = 0

        try:
            dictionary_of_names[new_person] = {}
            
        except:
            #for some odd reason, python doesn't let me create a file and start editing it in
            #one execution. Therefore the following couple lines had to be made to inform the
            #user to restart the program.
            print("dictionary file made! please restart the script.")
            time.sleep(5)
            break


        #finds the ID of the last person within the dictionary and adds 1 to it to make
        #the ID of a new person within the dictionary.

        for trait in ["name","age","gender"]:
            dictionary_of_names[new_person][trait] = str(input("what is your " + trait + "? "))
        #adds a new piece of info to every trait.


        for person, info in dictionary_of_names.items():
            print()
            print ("ID:", person)
            #prints person's ID
            for piece in info:
                #for every piece of info, name, gender, etc... it will print it and the corresponding information.
                #for example a piece will be name and the corresponding info will be john.
                print(piece + ":", dictionary_of_names[person][piece])


        with open("dictionary.txt", "w+") as Reader:
            dictionary = Reader.write(str(dictionary_of_names))


            
    elif (action == "quit" or action == "q"):
        break
    
    elif (action == "view" or action == "v"):
        try:
            with open("dictionary.txt") as Reader:
                dictionary = Reader.readline()
                dictionary = eval(dictionary)
                for ID, info in dictionary.items():
                    print()
                    print("ID:" + str(ID))
                    for piece in info:
                        print(piece + ": " + info[piece])
            print()
        except:
            print("No file found to be read")
            
    elif (action == "delete" or action == "d"):
            with open("dictionary.txt", "r+") as Reader:
                dictionary = Reader.readline()
                dictionary = eval(dictionary)
                user_to_delete = int(input("Which user ID to delete? "))
                try:
                    del dictionary[user_to_delete]
                    print(dictionary)
                    Reader.write(str(dictionary))

                except:
                    print("User doesn't exist.")
                
    else:
        print()
        print("Invalid input, please enter a valid command.")
        print()
                

        
        
