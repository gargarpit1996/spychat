from spydetails import spy_name, spy_age,spy_rating
print "hello buddy!!"
print 'let\'s get started'

STATUS_MESSAGE =['Sleeping','Talk is cheap,show me the Code','Keep Calm And Code Python']
friends_name = ['Ram']
friends_age =[26]
friends_rating=[2.5]
friends_is_online=[True]


def add_status(c_status):
    if c_status !=None:
        print "your current status is "+ c_status
    else:
        print"You dont have any status Currently"
    existing_status = raw_input("You want to select from old status ? Y/N")
    if existing_status.upper()=="N":
        new_status =raw_input("Enter your Status: ")
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)
    elif existing_status.upper()=="Y":
        serial_no=1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + " " + old_status
            serial_no = serial_no + 1
        user_choice = input("Enter Your Choice: ")
        new_status = STATUS_MESSAGE[user_choice-1]
    updated_status = new_status
    return updated_status


def add_friend():
    frnd_name = raw_input("What is your name ? ")
    frnd_age = input("What is your age? ")
    frnd_rating=input("What is your rating? ")
    if len(frnd_name)>2 and 12<frnd_age<50 and frnd_rating>spy_rating:
        frnd_name.append(frnd_name)
        friends_age.append(frnd_age)
        friends_rating.append(frnd_rating)
        friends_is_online.append(True)
    else:
        print "Friend cannot be added"
        return len(friends_name)





def start_chat(spy_name,spy_age,spy_rating):
    print "here r your options " + spy_name
    current_status= None
    show_menu =True
    while show_menu:
        choice= input("What do you want to do?\n 1.Add a status \n 2. Add a friend \n 3.Send a Message \n 4. Read a Message \n 5.Exit")
        if choice ==1 :
            current_status =add_status(current_status)
            print "Updated status is " + current_status
            add_status(current_status)
        elif choice == 2:
            no_of_frnd = add_friend()
            print "You have" + str(no_of_frnd) + "friends"
        elif choice ==0:
            show_menu = False
        else:
            print"Invalid Input"





spy_exist = raw_input("Are you a new user? Y/N")
if spy_exist.upper()=="N":                                #use nested if & else.
    print "Welcome Back"

elif spy_exist.upper() == "Y":                  # use .upper for change alphabet format in upper case.
     spy_name = raw_input('what is your spy name..!!')
     if len(spy_name)>2:
        print " Welcome "  +  spy_name  +  "  Glad to have u back with us. "
        spy_salutation = raw_input ("What should we call U (Mr. or Ms.)? ")
        if spy_salutation.upper=="Mr." or spy_salutation.upper=="Ms.":
            spy_name = spy_salutation  + "  " + spy_name
            print " Alright "  +  spy_name  + " I Would Like to know a Little bit more about you "
            spy_is_online=True
            spy_age = input ("What is your age ? ")                 #age of spy

            if 50> spy_age>12:
               print "You are Eligible to be a Spy"
               spy_rating = input("What is your Rating ? ")                    #rating of the spy
               if spy_rating>5.0:                              #nested if
                    print "Great Spy"
               elif 3.5<spy_rating<=5.0:
                   print "Average Spy"
               elif 2.5<spy_rating<=3.5:
                   print "Bad Spy"
               else:
                   print  "Aap kon....? "
               spy_is_online=True
               print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"

            else:
                print"You are not eligible to be a spy"                #not elegible to be a spy
        else:
            print"Ivalid salutation"                           #invalid situation
     else:
         print" OOOPPS... Please Enter a Valid Name"
