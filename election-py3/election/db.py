import sqlite3

conn = sqlite3.connect('election.db')

def create_user(username, password):
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def grant_write_permission(username):
    c = conn.cursor()
    c.execute("UPDATE users SET permission = 'write' WHERE username = ?", (username,))
    conn.commit()

def grant_read_permission(username):
    c = conn.cursor()
    c.execute("UPDATE users SET permission = 'read' WHERE username = ?", (username,))
    conn.commit()

def init():
    ##### create two user for read and write permission respectively
    # create_user('user1', 'password1')
    # grant_write_permission('user1')

    # create_user('user2', 'password2')
    # grant_read_permission('user2')

    c = conn.cursor()

    c.execute('''CREATE TABLE if not exists election
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
                election_id TEXT,
                candidate_id TEXT)''')

    conn.commit()
    print("table created")


def insert_data(election_id, candidate_id):
    c = conn.cursor()
    c.execute("INSERT INTO election (election_id, candidate_id) VALUES (?, ?)", (election_id, candidate_id,))
    print(c.lastrowid)
    conn.commit()

def read_data():
    c = conn.cursor()
    
    results = c.fetchall()
    return [row for row in results]
