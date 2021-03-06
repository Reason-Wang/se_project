import psycopg2
from psycopg2 import OperationalError

remote_host = '123.57.48.49'

# create connection to database
# eg: connection = create_connection(db_name='se', db_user='user0', db_password='123456')


def create_connection(db_name, db_user, db_password, db_host=remote_host, db_port=5432):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def close(connection):
    connection.close()

'''
USAGE:

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""
execute_query(connection, create_users_table)

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id SERIAL PRIMARY KEY, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER REFERENCES users(id)
)
"""
execute_query(connection, create_posts_table)

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

update_post_description = """
UPDATE
  posts
SET
  description = 'The weather has become pleasant now'
WHERE
  id = 2
"""
execute_query(connection,  update_post_description)
'''

if __name__ == '__main__':
    conn = create_connection(db_name='se', db_user='user0', db_password='123456')
    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts (
      id SERIAL PRIMARY KEY, 
      title TEXT NOT NULL, 
      description TEXT NOT NULL, 
      user_id INTEGER REFERENCES users(id)
    )
    """

    execute_query(conn, create_posts_table)

    posts = [
        ("Happy", "I am feeling very happy today", 1),
        ("Hot Weather", "The weather is very hot today", 2),
        ("Help", "I need some help with my work", 2),
        ("Great News", "I am getting married", 1),
        ("Interesting Game", "It was a fantastic game of tennis", 5),
        ("Party", "Anyone up for a late-night party today?", 3),
    ]

    post_records = ", ".join(["%s"] * len(posts))

    insert_query = (
        f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"
    )

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(insert_query, posts)

    select_users = "SELECT * FROM posts"
    posts = execute_read_query(conn, select_users)

    for post in posts:
        print(post)

    drop_posts_table = "drop table posts"
    execute_query(conn, drop_posts_table)

    close(conn)
