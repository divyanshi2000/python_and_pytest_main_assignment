# # Main Assignment
admin = {
    "name": "admin",
    "mail": "admin",
    "phone_number": "",
    "password": "admin"
}
user= {
    "name": "",
    "mail": "",
    "phone_number": "",
    "password": "",
    "booked_ticket": []
}
movie= {
    "title": "KGF",
    "admin_rating": 10,
    "lang": "Hindi",
    "show_timing": ['6-10', '12-4', '6-10'],
    "capa": 50
}
movies_list = []

movies_list.append(movie)


def login():
    print("******Welcome to Book My Show******* ")
    input_email = input("Enter Email\n: ")
    input_pass = input("Enter Password\n: ")

    if input_email == admin['mail'] and input_pass == admin["password"]:
        while True:
            print("Logged in Successfully")
            print("\n******Welcome Admin*******")
            ch = input("100. Add New Movie Info\n200. Delete Movies\n300. Logout\nEnter Choice: ")
            if ch == '100':
                print('Add New Movie')
                title = input("Title\n: ")
                admin_rating = int(input("Rating\n: "))
                lang = input("Language\n: ")
                show_timing = input("Sample: 6-10 12-4 6-10\nShow Timing\n: ").split()
                capa = int(input("Capacity\n: "))
                new_movie_dic = {
                    "title": title,
                    "admin_rating": admin_rating,
                    "lang": lang,
                    "show_timing": show_timing,
                    "capa": capa
                }
                movies_list.append(new_movie_dic)
                print('New Movie Successfuly added')


            elif ch == '200':
                print('Delete Movies')
                count = 0
                for movie in movies_list:
                    print(count, " ", movie['title'])
                    count += 1
                ch = int(input("Movie No.\n:"))
                movies_list.pop(ch)
                print('Movies Deleted Successfuly')

            elif ch == '300':
                print('Logout')
                # exit(0)
                break

    elif input_email == user['mail'] and input_pass == user['password']:
        while True:
            print("Logged in Successfully")
            movies = []
            timing = []
            count = 0
            for movie in movies_list:
                print(count, " ", movie['title'])
                movies.append(movie['title'])
                timing.append(movie['show_timing'])
                count += 1

            usr_input = int(input("5 logout\n6 Exit\n7. My Bookings\n\n:"))
            if usr_input == 6:
                exit(0)
            elif usr_input == 7:
                print(user['booked_ticket'])
            elif usr_input >= 0:
                ch = int(input("1. Book Tickets\n2. Cancel Tickets\n:"))
                if ch == 1:
                    tim = []

                    count = 0
                    for time in timing:
                        tim.append(time)
                        print(count, " ", time)
                        count += 1

                    choice = input("Timing\n: ")
                    res = movies[usr_input] + " " + str(choice)
                    user['booked_ticket'] = res.split()
                    print("Booked Tickets")

                elif ch == 2:
                    print("Ticket Canceled")
                    exit(0)
                else:
                    print("Not a valid input")
                pass
            elif usr_input == "2":
                # movie details
                pass
            else:
                print("Not a valid input")

    else:
        print("Enter a valid Email and Password.")

def register_new_account():
    print("****Create new Account*****")
    user['name'] = input("Name: ")
    user['mail'] = input("Email: ")
    user['phone'] = input("Phone: ")
    user['password'] = input("Password: ")
    # print(user_dic)

if __name__ == "__main__":
    while True:
        print("\n******Welcome to Book My Show*******\n")
        main_choice = input("1. Login\n2. Register new account\n3. Exit\n: ")
        print(main_choice)
        if main_choice == "1":
            login()
        elif main_choice == "2":
            register_new_account()
        elif main_choice == "3":
            print("Exit")
            exit(0)
        else:
            print("Enter a valid input")