import os
import json

#Function to load user data from JSON fie
def load_users():
    if os.path.exists('users.json'):
        with open('users.json','r') as file:
            return json.load(file)
    else:
        return {}

#Function to save user data to JSON file
def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)
def is_unique_username(username, users):
    return username not in users
def sign_up():
    users = load_users()
    while True:
        username = input("Enter a unique Username: ")
        if is_unique_username(username, users):
            users[username] = {'history' : []}
            save_users(users)
            print("User signed up successfully!")
        else:
            print("Username already exists. please try again")
def display_movies():
    print("Available Movies: ")
    for i, movie in enumerate(movies):
        print(f"{i+1}.{movie}")
def book_tickets(username):
    display_movies()
    choice = int(input("Enter the movie number to book tickets: ")) - 1
    if choice < 0 or choice >=len(movies):
        print("Invalid Choice!")
        return
    movie = movies[choice]
    print(f"Booking tickets for {movie}...")
    seats_available = seats[movie]
    print(f"Seats available: {seats_available}")

    num_tickets = int(input("Enter the number of tickets to book: "))
    if num_tickets > seats_available:
        print("Not enough seats available.")
        return
    
    seats[movie] -= num_tickets
    users[username]['history'].append(movie)
    save_users(users)
    print("Tickets booked successfully")


def main():
    global users, movies, seats
    users = load_users()
    movies = ["Avengers: Endgame", "The Shawshank Redemption", "Inception"]
    seats = {movie: 50 for movie in movies}

    while True:
        print("\n Welcome to Movie Ticketing Sytsem")
        print("1. Sign Up")
        print("2. Book Tickets")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            sign_up()
        elif choice == 2:
            username = input("Enter your username: ")
            if username in users:
                book_tickets(username)
            else:
                print("User not found. Please Sign up. ")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")
if __name__=="__main__":
    main()
