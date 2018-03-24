print "hello world!!"
print 'let\'s get started'
spy_name=raw_input("what is your spy name ?")
if len(spy_name)>2:
    print " Welcome "  +  spy_name  +  "  Glad to have u back with us. "
    spy_salutation = raw_input ("What should we call U (MR. or Ms.)? ")
    if spy_salutation=="Mr." or spy_salutation=="Ms.":
        spy_name = spy_salutation  + "  " + spy_name
        print " Alright "  +  spy_name  + " I Would Like to know a Little bit more about you "
        spy_age = input ("What is your age ? ")
        if 50> spy_age>12:
            print "Your Age is correct"
            spy_rating = input("What is your Rating ? ")
            if spy_rating>5.0:
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
            print"You are not eligible to be a spy"
    else:
        print"Ivalid salutation"
else:
    print" OOOPPS... Please Enter a Valid Name"
