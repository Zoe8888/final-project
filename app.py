# Importing various modules
import hmac
import sqlite3
import datetime
import cloudinary
import cloudinary.uploader
import validate_email
import DNS
from flask_mail import Mail, Message
from flask import Flask, request, redirect, jsonify
from flask_jwt import JWT, jwt_required
from flask_cors import CORS


# Creating a user class
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


# Creating a product class
class Post(object):
    def __init__(self, post_id, title, content, author, date_created, id):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date_created
        self.id = id


# Creating a database class
class Database(object):
    def __init__(self):
        # Opening blog database
        self.conn = sqlite3.connect('blog.db')
        self.cursor = self.conn.cursor()

    # Registration function
    def registration(self, name, surname, email, username, password):
        self.cursor.execute("INSERT INTO users(name, surname, email, username, password) VALUES(?, ?, ?, ?, ?)",
                            (name, surname, email, username, password))
        self.conn.commit()

    # Login function
    def login(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        registered_user = self.cursor.fetchone()
        return registered_user

    # View profile function
    def view_profile(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (str(username)))
        response = self. cursor.fetchone()
        return response

    # Edit user profile function
    def edit_profile(self, incoming_data, id):
        response = {}
        put_data = {}

        # If the name is edited
        if incoming_data.get('name') is not None:
            put_data['name'] = incoming_data.get('name')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET name =? WHERE id =?", (put_data['name'], id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Name successfully updated"

        # If the surname is edited
        if incoming_data.get('surname') is not None:
            put_data['surname'] = incoming_data.get('surname')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET surname =? WHERE id=?", (put_data['surname'], id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Surname successfully updated"

        # If the email is edited
        if incoming_data.get('email') is not None:
            put_data['email'] = incoming_data.get('email')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET email =? WHERE id=?", (put_data['email'], id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "ID number successfully updated"

        # If the username is edited
        if incoming_data.get('username') is not None:
            put_data['username'] = incoming_data.get('username')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET username =? WHERE id=?", (put_data['username'], id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Username successfully updated"

        # If the password is edited
        if incoming_data.get('password') is not None:
            put_data['password'] = incoming_data.get('password')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET password =? WHERE id=?", (put_data['password'], id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Password successfully updated"

        # If the user image is edited
        if incoming_data.get('user_image') is not None:
            put_data['user_image'] = incoming_data.get('user_image')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE users SET user_image =? WHERE id =?", (put_data['user_image'], id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "User image successfully updated"

        return response

    # Delete profile function
    def delete_profile(self, value):
        self.cursor.execute("DELETE FROM users WHERE id='{}'".format(value))
        self.conn.commit()

    # Add new post function
    def create_post(self, post_image, title, content, author, id):
        cloudinary.config(cloud_name='dxgylrfai', api_key='297452228378499', api_secret='lMfu9nSDHtFhnaRTiEch_gfzm_A')
        upload_result = None
        app.logger.info('%s file_to_upload', post_image)
        if post_image:
            upload_result = cloudinary.uploader.upload(post_image)
            app.logger.info(upload_result)
        date_created = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        self.cursor.execute("INSERT INTO posts(post_image, title, content, author, date_created, id) "
                            "VALUES(?, ?, ?, ?, ?, ?)",
                            (upload_result['url'], title, content, author, date_created, id))
        self.conn.commit()

    # Edit post function
    def edit_post(self, incoming_data, post_id):
        response = {}
        put_data = {}

        # Edit title of post
        if incoming_data.get('title') is not None:
            put_data['title'] = incoming_data.get('title')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE posts SET title =? WHERE post_id=?", (put_data['title'], post_id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Post title was successfully updated."

        # Edit image of post
        if incoming_data.get('post_image') is not None:
            put_data['post_image'] = incoming_data.get('post_image')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE posts SET post_image =? WHERE post_id=?", (put_data['post_image'], post_id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Post image was successfully updated."

        # Edit content of post
        if incoming_data.get('content') is not None:
            put_data['content'] = incoming_data.get('content')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE posts SET content =? WHERE post_id=?", (put_data['content'], post_id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Post content was successfully updated."

        # Edit author of post
        if incoming_data.get('author') is not None:
            put_data['author'] = incoming_data.get('author')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE posts SET author =? WHERE post_id=?", (put_data['author'], post_id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "Post author was successfully updated."

        # Edit user id of post
        if incoming_data.get('id') is not None:
            put_data['id'] = incoming_data.get('author')
            with sqlite3.connect('blog.db') as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE posts SET id =? WHERE post_id=?", (put_data['id'], post_id))
                conn.commit()
                response['status_code'] = 200
                response['message'] = "User id of post was successfully updated."

        return response

    # Deleting post function
    def delete_post(self, value):
        self.cursor.execute("DELETE FROM posts WHERE post_id='{}'".format(value))
        self.conn.commit()

    # Displaying all posts function
    def show_posts(self):
        self.cursor.execute("SELECT * FROM posts")
        return self.cursor.fetchall()

    # Display a post function
    def view_post(self, value):
        self.cursor.execute("SELECT * FROM posts WHERE post_id='{}'".format(value))
        response = self.cursor.fetchone()
        return response

    # Display a specific users posts
    def view_users_posts(self, value):
        self.cursor.execute("SELECT * FROM posts WHERE id='{}'".format(value))
        return self.cursor.fetchall()


# Creating a user table
def init_user_table():
    conn = sqlite3.connect('blog.db')
    print("Opened database successfully")

    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "user_image TEXT,"
                 "name TEXT NOT NULL,"
                 "surname TEXT NOT NULL,"
                 "email TEXT NOT NULL,"
                 "username TEXT NOT NULL,"
                 "password TEXT NOT NULL)")
    print("User table created successfully")
    conn.close()


# Create a blog post table
def init_post_table():
    with sqlite3.connect('blog.db') as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS posts(post_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "post_image TEXT NOT NULL,"
                     "title TEXT NOT NULL,"
                     "content TEXT NOT NULL,"
                     "author TEXT NOT NULL,"
                     "date_created TEXT NOT NULL,"
                     "id INTEGER TEXT NULL,"
                     "FOREIGN KEY (id) REFERENCES users(id))")
    print("Post table created successfully.")


# Fetching all users
def fetch_users():
    with sqlite3.connect('blog.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        new_data = []

        for data in users:
            new_data.append(User(data[0], data[5], data[6]))

    return new_data


# Fetching all blogs
def fetch_blog_posts():
    with sqlite3.connect('blog.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()

        new_data = []

        for data in posts:
            new_data.append(Post(data[0], data[1], data[2], data[3], data[4], data[5]))
    return new_data


# Initializing user table
init_user_table()
# Initializing product table
init_post_table()
# Creating list of all users
users = fetch_users()
# Creating a list of all the posts
blog_posts = fetch_blog_posts()


username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    # users = fetch_users()
    # username_table = {u.username: u for u in users}
    user = username_table.get(username, None)
    if user and hmac.compare_digest(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


# App initialized
app = Flask(__name__)
CORS(app, resource={r"/*": {"origins": "*"}})
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
# Extends the jwt tokens validation time to 20 hours
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(hours=24)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# Senders email
app.config['MAIL_USERNAME'] = 'crystalcavecpt@gmail.com'
# Senders password
app.config['MAIL_PASSWORD'] = 'crysta1Cav3'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

jwt = JWT(app, authenticate, identity)


# User registration route
@app.route('/registration/', methods=["POST"])
def registration():
    db = Database()
    response = {}

    if request.method == "POST":

        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect('blog.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username='{}'".format(username))
            registered_username = cursor.fetchone()

        # Creates an error if all fields aren't filled out
        if name == '' or surname == '' or email == '' or username == '' or password == '':
            response['status_code'] = 400
            response['message'] = "Error! Please enter all fields."
            return response

        # Checks if the email is valid
        elif not validate_email.validate_email(email, verify=True):
            response['status_code'] = 400
            response['message'] = "Error! Please enter a valid email address."
            return response

        # Checks if the username exists already
        elif registered_username:
            response['status_code'] = 400
            response['message'] = "Username already taken. Please enter a unique username."
            return response

        else:
            db.registration(name, surname, email, username, password)
            response["message"] = "New user successfully registered"
            response["status_code"] = 200

            global users
            users = fetch_users()

        return redirect("/send-email/%s" % email)


# App route to send an email once a user has successfully registered
@app.route('/send-email/<email>', methods=["GET"])
def send_email(email):
    response = {}
    mail = Mail(app)
    msg = Message("Welcome!", sender='crystalcavecpt@gmail.com', recipients=[email])
    msg.body = "Good morning/afternoon {}.\n You have successfully registered your profile on our site.\n" \
               "Please feel free to send us an email if you have any queries or concerns.\n \n" \
               "Kind Regards,\n Crystal Cave Team"
    mail.send(msg)

    response["message"] = "New user successfully registered"
    response["status_code"] = 200

    return response


# App route to login
@app.route('/login/', methods=["POST"])
def login():
    response = {}

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect('blog.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            registered_user = cursor.fetchone()

        # If username is empty it creates an error
        if username == '':
            response['status_code'] = 400
            response['message'] = "Error! Please enter your username."
            return response

        # If password is empty it creates an error
        if password == '':
            response['status_code'] = 400
            response['message'] = "Error! Please enter your password."
            return response

        # Checks if the user exists in the database
        if registered_user:
            response['registered_user'] = registered_user
            response['status_code'] = 200
            response['message'] = "Successfully logged in"
            return response

        else:
            response['status_code'] = 400
            response['message'] = "Login unsuccessful. Please try again."
        return jsonify(response)


# App route for the user to view their profile
@app.route('/view-profile/<username>/', methods=["GET"])
@jwt_required()
def view_profile(username):
    response = {}

    with sqlite3.connect('blog.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username='{}'".format(username))

        response['status_code'] = 200
        response['message'] = "Profile retrieved successfully"
        response['data'] = cursor.fetchone()

    return jsonify(response)


# App route for the user to edit their profile
@app.route('/edit-profile/<int:id>/', methods=["PUT"])
@jwt_required()
def edit_profile(id):
    response = {}

    if request.method == "PUT":
        incoming_data = dict(request.json)
        db = Database()
        response = db.edit_profile(incoming_data, id)

    return response


# App route for the user to delete their profile
@app.route('/delete-profile/<int:id>/')
@jwt_required()
def delete_profile(id):
    response = {}
    db = Database()
    db.delete_profile(id)

    response['status_code'] = 200
    response['message'] = "Profile successfully deleted"
    return response


# Display all users route
@app.route('/display-users/', methods=["GET"])
def display_users():
    response = {}
    with sqlite3.connect("blog.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")

        all_users = cursor.fetchall()

    response['status_code'] = 200
    response['data'] = all_users
    return response


# App route for the user to create a post
@app.route('/create-post/', methods=["POST"])
@jwt_required()
def create_post():
    db = Database()
    response = {}

    if request.method == "POST":
        image = request.files['post_image']
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        id = request.form['id']

        print(title, content, author, id)

        db.create_post(image, title, content, author, id)
        response["status_code"] = 200
        response['description'] = "Post created successfully"
        return response


# App route for the user to delete a blog post
@app.route('/delete-post/<int:post_id>/')
@jwt_required()
def delete_post(post_id):
    db = Database()
    response = {}
    db.delete_post(post_id)
    response['status_code'] = 200
    response['message'] = "Post successfully deleted"
    return response


# App route for the user to edit their post
@app.route('/edit-post/<int:post_id>/', methods=["PUT"])
@jwt_required()
def edit_post(post_id):
    response = {}

    if request.method == "PUT":
        incoming_data = dict(request.json)
        db = Database()
        response = db.edit_post(incoming_data, post_id)

    return response


# App route to display all the posts from the database
@app.route('/show-posts/', methods=["GET"])
@jwt_required()
def show_posts():
    db = Database()
    response = {}

    posts = db.show_posts()
    response['status_code'] = 200
    response['data'] = posts
    return response


# App route to view a specific post
@app.route('/view-post/<int:post_id>/', methods=["GET"])
@jwt_required()
def view_post(post_id):
    db = Database()
    response = {}

    data = db.view_post(post_id)
    response['data'] = data
    response['status_code'] = 200
    response['description'] = "Post was successfully retrieved"

    return jsonify(response)


# App route to view a specific users posts
@app.route('/view-users-posts/<int:id>/', methods=["GET"])
@jwt_required()
def view_users_products(id):
    response = {}
    db = Database()

    user_posts = db.view_users_posts(id)
    response['status_code'] = 200
    response['message'] = "All posts from user retrieved successfully"
    response['data'] = user_posts

    return response


if __name__ == '__main__':
    app.run()