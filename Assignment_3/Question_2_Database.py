import sqlite3
from Question_2_Buisness import Player

# set the name of the database to a variable to use in the program
DB_FILE = 'player_db.sqlite'


# create a function to open the database to use through the program
# use the connect function to connect to the database and use the Row Factory to compile
def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


# make a close function to close the database to not have it corrupt
# pass the "conn" from the connect function to show what database need to be closed
def close(conn):
    conn.close()


# set a function to add data to the database using SQL syntax
# pass in the conn for the open database and pass in a variable to insert
def add_player(conn, play_obj):
    play = conn.cursor()
    query = f"INSERT INTO Player (name, wins, losses, ties) VALUES(?,?,?,?)"
    play.execute(query, (play_obj.name, play_obj.wins, play_obj.losses, play_obj.ties))
    conn.commit()


# set a function to delete a player from the database using SQL syntax
# pass in the conn for the open database and pass in a variable for the name to delete from the database
def delete_player(conn, person):
    play = conn.cursor()
    query = f"DELETE FROM Player WHERE name = '{person}'"
    play.execute(query)
    conn.commit()


# create a player object to use to assign data that can be passed in the database
def player_obj(row):
    return Player(row['name'], row['wins'], row['losses'], row['ties'])


# set a function to get player data from the database to display in the main function
# use a fetch all to display all the data in the database and append it to a list
def get_player(conn):
    play = conn.cursor()
    query = f"SELECT * FROM Player ORDER BY wins DESC"
    play.execute(query)
    result = play.fetchall()
    player = []
    for row in result:
        player.append(player_obj(row))
    return player


# set a function that will take the data in the database and update it to new user variables
def updated_data(conn, name, wins, losses, ties):
    play = conn.cursor()
    query = f"UPDATE Player SET wins = '{wins}', losses = '{losses}', ties = '{ties}' Where name = '{name}'"
    play.execute(query)
    conn.commit()
