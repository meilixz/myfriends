# import the Flask library
from flask import Flask,render_template
import mysql.connector

#create connection
myconn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = 'print("Hello1World")'
)
#create cursor to execute sql
mycursor = myconn.cursor()

#create a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS myfriends;")
mycursor.execute("USE myfriends;")
mycursor.execute("CREATE TABLE IF NOT EXISTS friendslist(id INT AUTO_INCREMENT PRIMARY KEY, friendsname VARCHAR(25), age INT);")
sql1 = "INSERT INTO friendslist (friendsname, age) values (%s, %s)"
value = ('Arden', 13)
#mycursor.execute(sql1,value)
#mycursor.execute("INSERT INTO friendslist (id, friendsname, age)VALUES (001, 'Tienshung', 25)")
myconn.commit()



# Create the Flask instance and pass the Flask
# constructor, the path of the correct module
app = Flask(__name__)


# Default route added using a decorator, for view function 'welcome'
# We pass a simple string to the frontend browser
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route("/all_friends")
def myfriends():
    sql = "SELECT friendsname,age FROM friendslist;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #return myresult
    print(myresult)
    return render_template("index.html", list = myresult, title = "Here are all my friends:")
    #return render_template("index.html")

@app.route("/big_friends")
def over13():
    sql = "SELECT friendsname,age FROM friendslist GROUP BY friendsname, age HAVING age > 13;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #return myresult
    print(myresult)
    return render_template("index.html", list = myresult, title = "Here are all my friends over 13:")

@app.route("/small_friends")
def under13():
    sql = "SELECT friendsname,age FROM friendslist GROUP BY friendsname, age HAVING age <= 13;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    #return myresult
    print(myresult)
    return render_template("index.html", list = myresult, title = "Here are all my friends 13 or under:")
 


# Start with flask web app, with debug as True,# only if this is the starting page
if(__name__ == "__main__"):
    app.run(debug=True)