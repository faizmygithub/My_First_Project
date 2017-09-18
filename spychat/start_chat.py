from spy_details import spy_age
def start_chat(name, age, rating, status):



    if spy_age > 10 and spy_age < 60:
        welcome_message = "Authentication Completed.Welcome\n Name: " + name + "\nAge: " + str( age) + "\nRating: " + str(rating)
        print welcome_message

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n 1.Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chat from a user \n 6. Close a application \n "
            result = int(raw_input(menu_choices))

            if (result == 1):
                print "You choose to update the status"
                current_status_message = add_status(current_status_message)
            elif (result == 2):
                number_of_friend = add_friend()
       # error_message="Invalid age .Not Older to Acess it!!"
        #print error_message


    else:
        error_message="Invalid age.Not Older to Access it!!"
        print error_message

