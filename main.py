from spydetails import spy,Spy,ChatMessage
from steganography.steganography import Steganography

from datetime import datetime                                                      #import_date_time
t = datetime.now()
print t.strftime("%b %d %Y %H:%M:%S")                                             #format_of_date_time
import csv


print "hello buddy!!"
print 'let\'s get started'

STATUS_MESSAGE =['Sleeping','Talk is cheap,show me the Code','Keep Calm And Code Python']   #status_message

frnd1 =Spy('Aryan','Mr.',23,2.5)
frnd2 =Spy('Abhimanyu','Mr.',24,2.5)
friends = [frnd1,frnd2]
def load_frnd():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)

        for row in reader:
            spy=Spy(Name=row[0],Salutation=row[1],Age=row[3],Rating=row[2])
            friends.append(spy)




def add_status(c_status):                              #ADD STATUS
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



def add_friend():                                              #ADD FRIEND
    frnd =Spy(" "," ",0,0.0)

    frnd.Name = raw_input("What is your name ? ")
    frnd.sal= raw_input("What should we call u ? ")
    frnd.Age = input("What is your age? ")
    frnd.Rating=input("What is your rating? ")
    frnd.is_online=True

    if len(frnd.Name)>2 and 12<(frnd.Age)<50 and (frnd.Rating):
        friends.append(frnd)

        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([spy.name, spy.saluation, spy.rating, spy.age, spy.is_online])

    else:
        print "Friend cannot be added"
        return len(friends)

def select_frnd():
    serial_no= 1
    for frnd in friends:
        print str(serial_no) + " " +frnd.Name
        serial_no= serial_no+1
    user_selected_frnd = input("Enter your choice:")
    user_selected_frnd_index =user_selected_frnd -1
    return user_selected_frnd_index

def send_message():                                                          #SEND MESSAGE
    selected_frnd = select_frnd()
    original_image = raw_input("What is your name of original image? ")                      #name_of_original_name
    secret_text = raw_input("What is your Secret text? ")                                   #Secret_text
    output_path = "output.jpg"
    Steganography.encode(original_image,output_path,secret_text)
    print "MESSAGE ENCODE"

    new_chat = ChatMessage(secret_text,True)                                             #dictationary Type_variable_new chat  ( one message all info.)

    friends[selected_frnd].chats.append(new_chat)           #message_append
    print " Your secret message is ready!!!!! "                      #print_message


def read_message():                                                                          #READ MESSAGE
    selected_frnd = select_frnd()
    output_path = raw_input("Which image you want to decode ? ")
    secret_text = Steganography.decode(output_path)
    print "Secret text is " + secret_text
    new_chat =ChatMessage(secret_text,False)

    friends[selected_frnd].chats.append(new_chat)

    if secret_text in ['BRB']:
        print "BE RIGHT BACK!!!"
    elif secret_text in ['HELP']:
        print "BACKU UP TEAM WILL REACH SOON"
    elif secret_text in ['SOS']:
        print "SAVE OUR SHIP"
    else:
        print "secret_text"
        print "Your secret message has been saved !!!!"


def read_chat_history():
    read_for = select_frnd()
    

def start_chat(Spy_Name,Spy_Age):                                     #START CHAT
    current_status= None
    show_menu =True
    while show_menu:
        choice= input("What do you want to do?\n 1.Add a status \n 2. Add a friend \n 3.Send a Message \n 4. Read a Message \n 5.Exit")

        if choice ==1 :                                                            #choice1
            current_status =add_status (current_status)                            #add_status
            print "Updated status "+ current_status                          #update_status+current_status


        elif choice == 2:                                                        #choice2
            no_of_frnd = add_friend()                                            #add_friend
            print "You have" + str(no_of_frnd) + "friends"
            print "Your friend list is: \n" "" +str(friends)


        elif choice == 3:                                                       #choice3
            send_message()                                                   #send_message

        elif choice == 4:                                                     #choice4
            read_message()   #read_message


        elif choice ==5:
            read_chat_history()

            show_menu = False

        else:
            print"Invalid Input"                                         #invalid_input


spy_exist = raw_input("Are you a new user? Y/N")
if spy_exist.upper()=="N".lower() or spy_exist == "n".upper():      #use nested if & else.
    print " Welcome Back Agent "

    start_chat(Spy.Name,Spy.Rating,Spy.Age)

elif spy_exist =="Y".lower() or spy_exist == "y".upper():

    spy =Spy(" "," ",0,0.0)

    Spy.Name = raw_input('what is your spy Name....???')
    if len(Spy.Name) > 2:

        print " Welcome "  + Spy.Name  +  " Glad to have u back with us. "
        spy_salutation = raw_input ("What should we call U (Mr. or Ms.)? ")                #salutation_of_spy(Mr. or Ms.)
        if spy_salutation =="Mr.".upper() or spy_salutation =="Ms.".upper() or spy_salutation =="Mr.".lower() or spy_salutation == "Ms.".lower():
            Spy.Name = spy_salutation  + "  " + Spy.Name

            print " Alright "  +  Spy.Name  + " I Would Like to know a Little bit more about you "
            Spy.Age = 0
            Spy.Rating =0.0     #use for know about spy_qualification.

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
               print "Authentication complete. Welcome " + Spy.Name + " age: " + str(spy_age) + " rating : " + str(spy_rating) + " Proud to have you onboard"

            else:
                print"You are not eligible to be a spy"                #not elegible to be a spy
        else:
            print"Ivalid salutation"                           #invalid situation
    else:
        print"OOOPPS... Please Enter a Valid Name"
else:
    print "Invalid Entry"

