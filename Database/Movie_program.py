import sqlite3
from movie_list import Category, Movie




def connect_to_db():
    db_file = "movies.sqlite"
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def close(conn):
    if conn:
        conn.close()

def make_category(row):
    return Category(row['categoryID'], row['categoryName'])


def make_movie(row):
    return Movie(row['id'], row['name'], row['year'], row['minutes'], make_category(row))

def get_categories(conn):
    query = """SELECT categoryID, name FROM categories"""
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()

    categories = []
    for row in result:
        categories.append(make_movie(row))
    return categories


def get_category(conn, category_id):
    query = """SELECT categoryID, name as categoryName from Category WHERE id = ?"""
    cur = conn.cursor()
    cur.execute(query, (category_id,))
    row = cur.fetchone()
    if row:
        return make_movie(row)
    else:
        return None



def make_movie_list(list_movies):
    movies = []
    for row in list_movies:
        movies.append(make_movie(row))
    return movies

def get_movie_by_category(conn, category_id):
    query = """SELECT movieID, Movie.name, year, minutes, Movie.categoryID, category,name as categoryName FROM movie join category on Movie.categoryID = category.categoryID WHERE Movie.categoryID = ?"""
    cur = conn.cursor()
    cur.execute(query, (category_id,))
    result = cur.fetchall()

    return make_movie_list(result)


def add_movie(conn, movie):
    query = """INSERT INTO movie (categoryID, name, year, minutes, Movie) VALUES (?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(query, (movie.categoryID, movie.name, movie.year, movie.minutes))
    conn.commit()


def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND")
    print("cat-")
    print("year-")
    print("add-")
    print("del-")
    print("exit")

def display_cat(conn):
    print("CATEGORIES")
    categories = get_categories(conn)
    for category in categories:
        print(f"{category.category.id}. {category.name}")
    print()


def add_movie(conn):
    name = input("name: ")
    year = int(input("year: "))
    minutes = int(input("minutes: "))
    category_id = int(input("categoryID: "))

    movie = Movie(name, year, minutes,category_id)
    add_movie(conn, movie)
    print(f"{name} was added\n")

def main():
    conn = connect_to_db()
    display_cat(conn)
    while True:
        command = input("Command: ").lower()
        if command == "add":
            add_movie(conn)
        elif command == "cat":
            pass
        elif command == "exit":
            break
        else:
            print("Invalid")
            display_menu()
    close()
    print("Bye!")

if __name__ == "__main__":
    main()

