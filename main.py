from spydetails import spy_name, spy_age,spy_raiting
print "hello buddy!!"
print 'let\'s get started'
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
