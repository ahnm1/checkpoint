import psycopg2

# Configure connection to PostgreSQL
conn = psycopg2.connect(
   host="localhost",
   database="dictionary",
   user="postgres",
   password="******"
)

# Return list from dictionary
def read_dict(connection):
    cur = connection.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

# Add word to dictionary
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

# Remove word from dictionary
def delete_word(connection, ID):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()


# Save/Commit changes to database
def save_dict(connection):
    cur = connection.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Commands: 'list', 'add', 'delete', 'quit'\n")
    
    if cmd == "list":
        print(read_dict(conn))

    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)

    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)

    elif cmd == "quit":
        save_dict(conn)
        exit()
