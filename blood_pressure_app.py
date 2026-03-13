from reading import Reading
print("Welcome to the blood pressure reading application")
while True:
    systolic = int(input("Enter your systolic "))
    diastolic = int(input("Enter your diastolic "))
    pulse = int(input("Enter your pulse "))

    #create a reading object
    reading = Reading()
    reading.setSystolic(systolic)
    reading.setDiastolic(diastolic)
    reading.setPulse(pulse)
    print(reading)
    option = input("\n\nDo you want to save this reading? Y for yes and N for No ")
    should_save = False
    save_key = "" 
    reading_dict={}
    match option:
        case "y"| "Y"| "yes"| "yeah":
            should_save = True
        case _:
            should_save = False
        
    if should_save:
        save_key=input("Set a key to save the reading with ")
        if save_key =="":
            break
        else:
            reading_dict[save_key]=reading
    else:
        print("You chose not to save the reading ")
    
    should_continue = True 
    print()
    option = input("Do you want to record another blood pressure reading? ")
    match option.lower():
        case "n"|"no"|"nope":
            should_continue=False 
        case _:
            should_continue=True 

    
    if not should_continue:
        break
        


