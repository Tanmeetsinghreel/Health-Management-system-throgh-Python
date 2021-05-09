# health management system:-

# suppose you are a fitness trainer/nutritionist. you have to deal with three clients
#i.e(harry,rohan,hammad)for eaach client you have to design their excersise and diet plan

#instructions:

# create a food log(food diary) file for each client
#create a excersise log file for each client
#ask the user whether they want to log or retrive client data.
# write the function that takes the input of the clients name after the client name is entered.
#it will display a message as "what you want to log-diet or excersise"
#use this function
# def getdate():
#               import datetime
#               return datetime.datetime.now()
# the purpose of this function is to give time with every record of food or excersise added in the file
# write a function to retrive excersise or food file records for any client.

print("Welcome to HEALTH MANAGEMENT SYSTEM\n")

def datetime():
    import datetime
    return datetime.datetime.now()
try:
 p = int(input("Press 6 for Add data or Press 7 for Retrive data:\n"))

 def add():
    print("Which clients data you want to add: Harry,Rohan,Hammad\n")
    n = int(input(" Press 1 for Harry\n Press 2 for Rohan\n Press 3 for Hammad\n"))
    if n == 1:
        print("Which would you want to add on: Food or Excersise\n")
        m = int(input("Press 4 for Food or 5 for Excersise\n"))
        if m == 4:
            print(" Harry! What did you eat")
            value = input("Type here:\n")
            with open("Harry's_food_fle.txt","a") as f:
             f.write("\n" + value + str(datetime()))
             print("Successfully added\n")
        elif m == 5:
            print("Harry! What did you do")
            value = input("Type here:\n")
            with open("Harry's_excersise_file.txt","a") as g:
             g.write("\n" + value + str(datetime()))
             print("Successfully added\n")
        else:
            print("invalid input")
    elif n == 2:
        print("What would you want to add: Food or Excersise\n")
        m = int(input("Press 4 for Food or 5 for Excersise\n"))
        if m == 4:
            print("Rohan! What did you eat")
            value = input("Type here:\n")
            with open("Rohan's_food_file.txt","a") as h:
                h.write("\n" + value + str(datetime()))
                print("Successfully added\n")
        elif m == 5:
            print("Rohan! What did you do")
            value = input("Type here:\n")
            with open("Rohan's_excersise_file.txt","a") as i:
                i.write("\n" + value + str(datetime()))
                print("Successfully added\n")
        else:
            print("Invalid output")
    elif n == 3:
        print("What would you want to add: Food or Excersise\n")
        m = int(input("Press 4 for Food or 5 for Excersise\n"))
        if m == 4:
            print("Hammad! What did you eat")
            value = input("Type here:\n")
            with open("Hammad's_food_file.txt","a") as  j:
                j.write("\n" + value + str(datetime()))
                print("Successfully added\n")
        elif m == 5:
            print("Hammad! What did you do")
            value = input("Type here:\n")
            with open("Hammad's_excersise_file.txt","a") as  k:
                print("Successfully added\n")
                k.write("\n" + value + str(datetime()))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
 def retrive():
    print("Which clients data you want to Read: Harry,Rohan,Hammad\n")
    n = int(input(" Press 1 for Harry\n Press 2 for Rohan\n Press 3 for Hammad\n"))
    if n == 1:
        print("What would you want to read: Food or Excersise\n")
        m = int(input("Press 4 for Food or 5 for Excersise\n"))
        if m == 4:
            with open("Harry's_food_fle.txt") as f:
              for item in f:
               print(item)
        elif m == 5:
            with open("Harry's_excersise_file.txt") as g:
              for item in g:
               print(item)
        else:
            print("Invalid input")
    elif n == 2:
        print("What would you want to read: Food or Excersise\n")
        m = int(input("Press 4 for Food or 5 for Excersise\n"))
        if m == 4:
            with open("Rohan's_food_file.txt") as h:
                for item in h:
                    print(item)
        elif m == 5:
            with open("Rohan's_excersise_file.txt") as i:
                for item in i:
                    print(item)
        else:
            print("Invalid input")
    elif n == 3:
        print("What would you want to read: Food or Excersise\n")
        m = int(input("Press 4 for Food or 5 for Excersise\n"))
        if m == 4:
            with open("Hammad's_food_file.txt") as  j:
                for item in j:
                    print(item)
        elif m == 5:
            with open("Hammad's_excersise_file.txt") as  k:
                for item in k:
                    print(item)
        else:
            print("Invalid input")
    else:
        print("Invalid input")

 if p == 6:
    add()
 elif p == 7:
    retrive()
 else:
    print("You have entered an invalid input")
except Exception as e:
 print("wrong input!")
# Description:-
# in this program first i create add function and then create retrive function and take input
#to the user for add data or retrive it