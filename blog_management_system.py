import hashlib
import sqlite3

conn = sqlite3.connect('blog.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS posts
             (id INTEGER PRIMARY KEY, title TEXT, content TEXT, user_id INTEGER)''')
def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, hashed_password))
    user_id = c.fetchone()
    return user_id[0] if user_id else None
def create_post(title, content, user_id):
    c.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, user_id))
    conn.commit()

def get_all_posts():
    c.execute("SELECT title, content FROM posts")
    posts = c.fetchall()
    return posts

def close_connection():
    conn.close()

def main():
    print("Welcome to the Basic Blog Management System!")
    user_id = None  

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Create Post")
        print("4. View Posts")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(username, password)
            print("User registered successfully!")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_id = authenticate_user(username, password)
            if user_id:
                print("Login successful!")
            else:
                print("Login failed! Invalid username or password.")

        elif choice == '3':
            if user_id:
                title = input("Enter post title: ")
                content = input("Enter post content: ")
                create_post(title, content, user_id)
                print("Post created successfully!")
            else:
                print("Please log in first!")

        elif choice == '4':
            posts = get_all_posts()
            if posts:
                print("\nAll Posts:")
                for post in posts:
                    print("Title:", post[0])
                    print("Content:", post[1])
                    print("-----------------------")
            else:
                print("No posts available.")

        elif choice == '5':
            close_connection()
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
