import psycopg2

# Configure connection to PostgreSQL
# Comment a litle more
conn = psycopg2.connect(
   host="localhost",
   database="dictionary",
   user="postgres",
   password="4231-rweq"
)

# Return list from dictionary
def read_dict(C):
    # Comment a litle more
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

# Add word to dictionary
def add_word(C, word, translation):
    # Comment a litle more
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

# Remove word from dictionary
def delete_word(C, ID):
    # Comment a litle more
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()


# Save/Commit changes to database
def save_dict(C):
    # Comment a litle more
    cur = C.cursor()
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
