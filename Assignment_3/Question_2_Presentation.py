# import from both the buisness and the database files
from Question_2_Buisness import Player
import Question_2_Database as db


# print a title and the menu
def title():
    print("Player Manager")
    print()
    print("COMMAND MENU")
    print("view - View Players")
    print("add  - Add a Player")
    print("updt - Update a Players Stats")
    print("del  - Delete a Player")
    print("exit - Exit Program")
    print()


# print the labels and the separator
# set the function from the database to a variable and pass a database connection into it
# use the display function to correctly display the data
def view(connection):
    print(f"{'Name':20}{'Wins':<10}{'Losses':<10}{'Ties':<10}{'Games':<10}")
    print('-' * 55)
    player = db.get_player(connection)
    display(player)


# set a function to format the data to fit the table
def display(players):
    for player in players:
        print(f"{player.name:14}{player.wins:>10}{player.losses:>12}{player.ties:>8}{player.games():>11}")


# this function takes user inputs and add's it to the database
# using while loops the user is unable to use negative numbers
# the function sets a Player object and assigns it to a variable that can be passed to the add_player function in the
# database
def add(connection):
    name = input("Name: ")
    wins = int(input("Wins: "))
    while wins < 0:
        print("Invalid Number. Try again.")
        wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    while losses < 0:
        print("Invalid Number. Try again.")
        losses = int(input("Losses: "))
    ties = int(input("Ties: "))
    while ties < 0:
        print("Invalid Number. Try again.")
        ties = int(input("Ties: "))
    player = Player(name=name, wins=wins, losses=losses, ties=ties)
    db.add_player(connection, player)
    print(f"{name} was added to the database.")


# the delete function calls the delete function in the database
# it uses the players name to find the data in the database
def delete(connection):
    name = input("Name: ")
    db.delete_player(connection, name)
    print(f"{name} was deleted from the database.")


# the update function takes a players choice and uses the update function in the database to update the data
def updated(connection):
    choice = input("Name: ").title()
    wins = int(input("Wins: "))
    while wins < 0:
        print("Invalid Number. Try again.")
        wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    while losses < 0:
        print("Invalid Number. Try again.")
        losses = int(input("Losses: "))
    ties = int(input("Ties: "))
    while ties < 0:
        print("Invalid Number. Try again.")
        ties = int(input("Ties: "))
    db.updated_data(connection, choice, wins, losses, ties)
    print(f"{choice} was updated in the Database")


# main function to run the program
def main():
    # set a variable to call the connect function in the database to open the database for use
    conn = db.connect()

    title()
    # while loop so the user can use the program repeatedly without closing
    while True:
        choice = input("Command: ")
        if choice == "view":
            view(conn)
            print()
        elif choice == "add":
            add(conn)
            print()
        elif choice == "del":
            delete(conn)
            print()
        elif choice == "updt":
            updated(conn)
            print()
        elif choice == "exit":
            break
        else:
            print("invalid choice. Try again!")
            print()

    print("Bye!")


if __name__ == "__main__":
    main()
