from spydetails import spy
from steganography.staganography import Steganography

print "hello buddy!!"
print 'let\'s get started'

STATUS_MESSAGE =['Sleeping','Talk is cheap,show me the Code','Keep Calm And Code Python']
friends =[{'name': 'Aryan','age': 23,'rating': 2.5,'is online':True},{'name': 'Abhimanyu','age': 24,'rating': 2.5,'is online':True}]

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
    frnd ={
        'name':'',
        'age' :0,
        'rating':0.0,
        'is online':True

    }
    frnd['name'] = raw_input("What is your name ? ")
    frnd['age'] = input("What is your age? ")
    frnd['rating']=input("What is your rating? ")
    if len(frnd['name'])>2 and 12<frnd['age']<50 and frnd['rating']>spy['rating']:
        friends.append(frnd)

    else:
        print "Friend cannot be added"
        return len(friends)

def select_frnd():
    serial_no= 1
    for frnd in friends:
        print str(serial_no) + " " +frnd['name']
        serial_no= serial_no+1
    user_selected_frnd = input("Enter your choice:")
    user_selected_frnd_index =user_selected_frnd -1
    return user_selected_frnd_index




def send_message():
    selected_frnd = select_frnd()
    original_image = raw_input("What is your name of original image? ")
    secret_text = raw_input("What is your Secret text? ")
    output_path = "ouutput.jpg"
    Steganography.encode(original_image,output_path,secret_text)
    print("message encoded")
    



def read_message():
    selected_frnd = select_frnd()




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

        elif choice == 3:
            send_message()

        elif choice == 4:
            read_message()

        elif choice ==0:
            show_menu = False

        else:
            print"Invalid Input"





spy_exist = raw_input("Are you a new user? Y/N")
if spy_exist.upper()=="N":      #use nested if & else.
    print "Welcome Back" +['name'] + "age :"+ str(spy['age']) +"having rating of " +str(spy['rating'])
    start_chat(spy['name'],spy['age'],spy['rating'])

elif spy_exist.upper()=="Y":
    spy ={
        'name':'',
        'age':0,
        'rating':0.0
    }




elif spy_exist.upper() == "Y":                  # use .upper for change alphabet format in upper case.
     spy['name'] = raw_input('what is your spy name..!!')
     if len(spy['name'])>2:
        print " Welcome "  +  spy['name']  +  "  Glad to have u back with us. "
        spy_salutation = raw_input ("What should we call U (Mr. or Ms.)? ")
        if spy_salutation.upper=="Mr." or spy_salutation.upper=="Ms.":
            spy['name'] = spy_salutation  + "  " + spy['name']
            print " Alright "  +  spy['name']  + " I Would Like to know a Little bit more about you "
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
               print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
               start_chat(spy['name'],spy_age,spy_rating)

            else:
                print"You are not eligible to be a spy"                #not elegible to be a spy
        else:
            print"Ivalid salutation"                           #invalid situation
     else:
         print" OOOPPS... Please Enter a Valid Name"
