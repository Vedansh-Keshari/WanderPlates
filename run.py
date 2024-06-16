import mysql.connector
import json
import textwrap
import urllib.request
from flask import Flask,render_template,request,render_template_string

from urllib.request import HTTPError

import cv2
from pyzbar import pyzbar

import speech_recognition as sr
from flask import redirect,url_for
import pyaudio
import time


# Other File
# from app import app

app=Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('login.html')



# LOGIN BUTTON
@app.route('/login_button',methods=['POST'])
def login_button():
    global email,password
    global role
    global u,p
    u=""
    p=""
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    email=request.form['email']
    password=request.form['password']

    print(email)
    print(password)

    if request.form['click']=='btn_click':

        time.sleep(3)
        # email asd
        # passw asdasd

        select_query=f"SELECT * FROM USERS WHERE EMAIL='{email}'"
        mycursor.execute(select_query)
        existing_record=mycursor.fetchone()

        if(existing_record):
            try:
                username_query = f"SELECT USERNAME FROM USERS WHERE EMAIL='{email}'" #parameter Passing
                mycursor.execute(username_query)  # type NONE
                username_record = mycursor.fetchone()
                # print(username_record)                   # username_record ---> tuple

                # If password is wrong Type Error Occurs

                u = "".join(username_record)  # tuple to str conversion
                # print(u)

                password_query=f"SELECT PASSWORD FROM USERS WHERE EMAIL='{email}' AND PASSWORD= '{password}' "
                # password_query = f"SELECT PASSWORD FROM USERS WHERE PASSWORD='{password}'"
                mycursor.execute(password_query)
                password_record = mycursor.fetchone()
                # print(password_record)              # password_record ---> tuple
                p = "".join(password_record)  # tuple to str conversion
                # print(p)

                if (u == email and password == p):
                    print("Correct email and pass")

                    #localhost_address=localhost_addr
                    return render_template('home.html')    #Localhost address of Home page

            # 200 404 error
            # asd xzczxczc
            except TypeError as e:
                incorrect_pass="""
                <html>
                <head>
                <script>
                alert("Incorrect Password.... ")
                </script>
                </head>
                <body>
                </body>
                </html>
                """
                print("tada")
                return render_template_string(incorrect_pass)


        else:
            print("Please Register...")
            register_alert = """
                                <html>
                                <head>
                                <script>
                                alert("PLEASE REGISTER TO ACCESS...")
                                </script>
                                </head>
                                <body>
                                </body>
                                </html>
                                """

            return render_template_string(register_alert)


        # query="INSERT INTO USER(username,password,role) VALUES('"+username+"','"+password+"','"+role+"')"
    return render_template('home.html')

# FORGOT PASSWORD LINK
@app.route('/forgotpass1')
def forgotpass():
    print("Forgot Pass link")
    return render_template('forgotpass1.html')


# SIGN UP LINK
@app.route('/signup')
def signup_link():
    print("Sign up link")
    return render_template('signup.html')


# Login Page⬆️
# Sign Up Page ⬇️

# SIGNUP BUTTON
@app.route('/signup_button', methods=['POST'])
def signup():
    global fullname,username,email
    global username,password

    # print("Check point 2")

    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    fullname = request.form['fullname']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    print(username)
    print(password)
    print(email)

    if request.form['click']=='btn_click':
        print("asdasd")
        query=("INSERT INTO USERS(name,username,email,password) VALUES('"+fullname+"','"+username+"','"+email+"','"+password+"')")
        mycursor.execute(query)
        db.commit()
    return render_template('signup.html') # new page Submit successfully

# LOGIN LINK
@app.route('/login')
def login_link():
    print("Login Back")
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/hotel')
def hotels():
    return render_template('hotels.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/trains')
def trains():
    return render_template('trains.html')

@app.route('/buses')
def bus():
    return render_template('Bus.html')
@app.route('/cabs')
def cabs():
    return render_template('Cabs.html')

# LOGIN BUTTON
@app.route('/book_flight',methods=['POST'])
def book_flight():
    global flyfrom,flyto
    global departing
    global u,p
    u=""
    p=""
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    flyfrom=request.form['flying_from']
    flyto=request.form['flying_to']
    departing=request.form['departing']

    print(flyfrom)
    print(flyto)
    print(departing)

    if request.form['click']=='btn_click':

        time.sleep(3)
        select_query=f"SELECT * FROM USERS WHERE USERNAME='{username}'"
        mycursor.execute(select_query)
        existing_record=mycursor.fetchone()

        if(existing_record):
            try:
                username_query = f"SELECT USERNAME FROM USERS WHERE USERNAME='{username}'"
                mycursor.execute(username_query)  # type NONE
                username_record = mycursor.fetchone()
                # print(username_record)                   # username_record ---> tuple

                # If password is wrong Type Error Occurs

                u = "".join(username_record)  # tuple to str conversion
                # print(u)

                password_query=f"SELECT PASSWORD FROM USERS WHERE USERNAME='{username}' AND PASSWORD= '{password}' "
                # password_query = f"SELECT PASSWORD FROM USERS WHERE PASSWORD='{password}'"
                mycursor.execute(password_query)
                password_record = mycursor.fetchone()
                # print(password_record)              # password_record ---> tuple
                p = "".join(password_record)  # tuple to str conversion
                # print(p)

                if (u == username and password == p):
                    print("Correct user and pass")

                    #localhost_address=localhost_addr

                return render_template('index.html')    #Localhost address of isbn page


            except TypeError as e:
                incorrect_pass="""
                <html>
                <head>
                <script>
                alert("Incorrect Password.... ")
                </script>
                </head>
                <body>
                </body>
                </html>
                """
                print("tada")
                return render_template_string(incorrect_pass)


        else:
            print("Please Register...")
            register_alert = """
                                <html>
                                <head>
                                <script>
                                alert("PLEASE REGISTER TO ACCESS...")
                                </script>
                                </head>
                                <body>
                                </body>
                                </html>
                                """

            return render_template_string(register_alert)


        # query="INSERT INTO USER(username,password,role) VALUES('"+username+"','"+password+"','"+role+"')"
    return render_template('login.html')

# Future...
# # MIC BUTTON🎈
# @app.route('/mic_button',methods=['POST'])
# def mic_button():
#     global username, password
#     global role
#     global u, p
#     username = "user1"
#     password = "pass1"
#     role = "check"
#     u = ""
#     p = ""
#
#
#     if request.form['click']=='btn_click':
#
#         text = voice_command()
#
#         # username = request.form['username']
#         # password = request.form['password']
#         # role = request.form['role']
#
#         print(username)
#         print(password)
#         print(role)
#
#         voice_login(text)
#             # return "Working"
#         return render_template("login.html",recognized_text=text)
#         # elif "save to db" in text.lower():
#         #     voice_db()
#         #     print("save to db")
#         # elif "save to excel" in text.lower():
#         #     voice_excel()
#         #     print("save to excel")
#         # elif "clear" in text.lower():
#         #     voice_clear()
#         #     print("clear ah")
#         # else:
#         #     print("break")
#
#     return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True,port=3000)

# TABLE CREATION
# CREATE TABLE USERS(ID INT PRIMARY KEY AUTO_INCREMENT,NAME VARCHAR(50),USERNAME VARCHAR(50),PASSWORD VARCHAR(50),EMAIL VARCHAR(50),ROLE VARCHAR(50));
 # elif( username == u or password == p):
        #     print("Username Exists...")
        #     alert = """
        #                 <html>
        #                 <head>
        #                 <script>
        #                 alert("INCORRECT PASSWORD...")
        #                 </script>
        #                 </head>
        #                 <body>
        #                 </body>
        #                 </html>
        #                 """
        #
        #     return render_template_string(alert)
        #
        # elif(username == u is False or password == p is True):
        #     print("Password Exists...")
        #     alert2= """
        #                             <html>
        #                             <head>
        #                             <script>
        #                             alert("INCORRECT USERNAME...")
        #                             </script>
        #                             </head>
        #                             <body>
        #                             </body>
        #                             </html>
        #                             """
        #
        #     return render_template_string(alert2)
        # select * from books where username={username}
        #
        # if password == password

        # ---
# if(f"SELECT USERNAME FROM USERS WHERE USERNAME='{username}'"==request.form['username']):
        #     if(f"SELECT PASSWORD FROM USERS WHERE PASSWORD='{password}'"==request.form['password']):
        #         print("Login Success")
