#spy_name="Faiz Ahmad"
#spy_age=20
#spy_rating=4.9
#spy_salutation="MR."
#spy_online=True
spy_name = raw_input("Welcome to spy chat, HEY,What's your name? ")

if len(spy_name) > 0:



    print 'Welcome ' + spy_name + '. Glad to have you back with us.'

    spy_salutation = raw_input("Should I call you MR. or MS.?: ")

    spy_name = spy_salutation + " " + spy_name

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

else:

    print "A spy needs to have a valid name. Try again please"
spy_age=0
spy_rating=0.0
spy_is_online=False
spy_age = raw_input("What is your age?")
print type(spy_age)
spy_age=int(spy_age)
print type(spy_age)



if spy_age > 10 and spy_age < 60:


    spy_rating = raw_input("What is your spy rating?")
    print type(spy_rating)
    spy_rating = float(spy_rating)
    print type(spy_rating)
else:

     print "Sorry you are not of the correct age to be a spy"

if spy_rating > 4.5:
    print "Best One :))!!"
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print "Good One :)!."
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print "Average One :)"
else:
    print "New one."

spy_online=True
print "Authentication complete. Welcome " + spy_name + " Your age is : " + str(spy_age) + " and with the rating of : " + str(spy_rating) + " HI What's been up?"
