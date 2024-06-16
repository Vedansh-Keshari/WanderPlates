import mysql.connector
import json
import textwrap
import urllib.request
from flask import Flask,render_template,request,render_template_string,url_for
from urllib.request import HTTPError

import cv2
from pyzbar import pyzbar

import speech_recognition as sr
import pyaudio
import time


# Other File
# from app import app

app=Flask(__name__,template_folder='template')
# @app.route('/')
# def index():
#     return render_template('home.html')

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

@app.route('/Itineraries')
def itineraries():
    return render_template('Itineraries.html')

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

# BOOK FLIGHT BUTTON
@app.route('/book_flight', methods=['POST'])
def book_flight():
    global departure,arrival
    global departing_date,passengers,coach

    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    departure=request.form['flying_from']
    arrival=request.form['flying_to']
    departing_date=request.form['departing']
    passengers=request.form['passengers']
    coach = request.form['coach']



    if request.form['click']=='btn_click':
        # TABLE CREATION flights
        time.sleep(3)
        query=(
                "INSERT INTO FLIGHTS (DEPARTURE,ARRIVAL,DEPARTING_DATE,PASSENGERS,COACH) VALUES('"+departure+"','"+arrival+"','"
            +departing_date+"','"+passengers+"','"+coach+"')")
        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("FLIGHT TICKET BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_train', methods=['POST'])
def book_train():
    global departure,arrival
    global departing_date,passengers,coach
    global seat_preference

    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    departure=request.form['departure_from']
    arrival=request.form['arrival_to']
    seat_preference=request.form['seat_preference']
    departing_date=request.form['departing']
    passengers=request.form['passengers']
    coach = request.form['coach']


    print(departure)
    print(arrival)
    print(departing_date)
    print(passengers)
    print(coach)

    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO TRAINS (DEPARTURE,ARRIVAL,DEPARTING_DATE,PASSENGERS,COACH,SEAT_PREFERENCE) VALUES('"+departure+"','"+arrival+"','"
            +departing_date+"','"+passengers+"','"+coach+"','"+seat_preference+"')")
        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("TRAIN TICKET BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_bus', methods=['POST'])
def book_bus():
    global departure,arrival
    global departing_date,passengers,type
    global seat_preference

    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    departure=request.form['departure_from']
    arrival=request.form['arrival_to']
    seat_preference=request.form['seat_preference']
    departing_date=request.form['departing']
    passengers=request.form['passengers']
    type = request.form['type']


    print(departure)
    print(arrival)
    print(departing_date)
    print(passengers)
    print(type)

    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO BUSES (DEPARTURE,ARRIVAL,SEAT_PREFERENCE,DEPARTING_DATE,PASSENGERS,TYPE) VALUES('"+departure+"','"+arrival+"','"+seat_preference+"','"+departing_date+"','"+passengers+"','"+type+"')")
        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("BUS TICKET BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)
@app.route('/book_cab', methods=['POST'])
def book_cab():
    global pick_up,pick_up_date,pick_up_time
    global drop_off,drop_off_date,drop_off_time
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    pick_up=request.form['picking_up']
    pick_up_date=request.form['picking_up_date']
    pick_up_time=request.form['picking_up_time']
    drop_off=request.form['drop_off']
    drop_off_date=request.form['drop_off_date']
    drop_off_time = request.form['drop_off_time']


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO CABS (PICK_UP,PICK_UP_DATE,PICK_UP_TIME,DROP_OFF,DROP_OFF_DATE,DROP_OFF_TIME) VALUES('"+pick_up+"','"+pick_up_date+"','"+
                pick_up_time+"','"+drop_off+"','"+drop_off_date+"','"+drop_off_time+"')")
        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("CAB BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_hotel', methods=['POST'])
def book_hotel():
    global hotel_name,check_in_date,check_out_date,rooms
    global adults,children
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name=request.form['hotel_name']
    check_in_date=request.form['check_in_date']
    check_out_date=request.form['check_out_date']
    rooms=request.form['rooms']
    adults=request.form['adults']
    children=request.form['children']


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO HOTELS (HOTEL_NAME,CHECK_IN_DATE,CHECK_OUT_DATE,ROOMS,ADULTS,CHILDREN) VALUES('"+hotel_name+"','"+check_in_date+"','"+check_out_date+"','"+rooms+"','"+adults+"','"+children+"')")
        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order_food', methods=['POST'])
def order_food():
    global restaurant_name,cuisines,price

    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    restaurant_name=request.form['restaurant_name']
    cuisines=request.form['cuisines']
    price=request.form['price']



    if request.form['click']=='btn_click':
        # TABLE CREATION flights
        time.sleep(3)
        query=(
                "INSERT INTO FOODS (RESTAURANT_NAME,CUISINES,PRICE) VALUES('"+restaurant_name+"','"+cuisines+"','"+
                price+"')")
        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("ORDERED NOW...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_hotel1', methods=['POST'])
def book_hotel1():
    global hotel_name,hotel_address,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name="Indian Descent"
    hotel_address="The Lodhi - Lodhi Road, New Delhi 110065 India"
    rating="4.0"
    cost="7,360.24"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_HOTELS (HOTEL_NAME,HOTEL_ADDRESS,RATING,COST) VALUES('"+hotel_name+"','"+hotel_address+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_hotel2', methods=['POST'])
def book_hotel2():
    global hotel_name,hotel_address,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name="Bukhara, Delhi"
    hotel_address="Diplomatic Enclave Sardar Patel Marg ITC Maurya, a Luxury Collection"
    rating="2.5"
    cost="4,851.07"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_HOTELS (HOTEL_NAME,HOTEL_ADDRESS,RATING,COST) VALUES('"+hotel_name+"','"+hotel_address+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

# CREATE TABLE POPULAR_HOTELS(ID INT PRIMARY KEY AUTO_INCREMENT,HOTEL_NAME VARCHAR(50),HOTEL_ADDRESS VARCHAR(50),RATING VARCHAR(50),COST VARCHAR(50));
@app.route('/book_hotel3', methods=['POST'])
def book_hotel3():
    global hotel_name,hotel_address,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name="The Bombay Canteen, Mumbai"
    hotel_address="Plot C 68, Unit 2, Jet Airways - Godrej, Bandra Kurla Complex, Mumbai, Maharashtra 400013"
    rating="4.4"
    cost="8,363.91"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_HOTELS (HOTEL_NAME,HOTEL_ADDRESS,RATING,COST) VALUES('"+hotel_name+"','"+hotel_address+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_hotel4', methods=['POST'])
def book_hotel4():
    global hotel_name,hotel_address,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name="Karim's, New Delhi"
    hotel_address="16 Matia Mahal Bazar, Near Jama Masjid Jama Masjid, New Delhi"
    rating="3.75"
    cost="6,272.93"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_HOTELS (HOTEL_NAME,HOTEL_ADDRESS,RATING,COST) VALUES('"+hotel_name+"','"+hotel_address+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)
@app.route('/book_hotel5', methods=['POST'])
def book_hotel5():
    global hotel_name,hotel_address,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name="Leopold Cafe"
    hotel_address="Shaheed Bhagat Singh Road Colaba Causeway, Mumbai 400005 India"
    rating="4.4"
    cost="8,280.27"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_HOTELS (HOTEL_NAME,HOTEL_ADDRESS,RATING,COST) VALUES('"+hotel_name+"','"+hotel_address+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/book_hotel6', methods=['POST'])
def book_hotel6():
    global hotel_name,hotel_address,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    hotel_name="Mavalli Tiffin Room"
    hotel_address="#14, Lalbagh Road, Bengaluru - 560027"
    rating="4.4"
    cost="9,618.50"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_HOTELS (HOTEL_NAME,HOTEL_ADDRESS,RATING,COST) VALUES('"+hotel_name+"','"+hotel_address+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("HOTEL BOOKED...")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)


# CREATE TABLE POPULAR_FOODS(ID INT PRIMARY KEY AUTO_INCREMENT,FOOD_NAME VARCHAR(50),CUISINE VARCHAR(50),RATING VARCHAR(50),COST VARCHAR(50));

@app.route('/order1', methods=['POST'])
def order1():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="Butter Garlic Naan"
    cuisine="Indian"
    rating="4"
    cost="250"




    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order2', methods=['POST'])
def order2():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="Amritsari Kulcha"
    cuisine="North Indian"
    rating="4.4"
    cost="650"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights
        # CREATE TABLE USERS(ID INT PRIMARY KEY AUTO_INCREMENT,DEPARTURE VARCHAR(50),ARRIVAL VARCHAR(50),DEPARTING_DATE VARCHAR(50),PASSENGERS VARCHAR(50),COACH VARCHAR(50));
        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order3', methods=['POST'])
def order3():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="Butter Chicken (Murgh Makhani)"
    cuisine="North Indian"
    rating="4.4"
    cost="850"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order4', methods=['POST'])
def order4():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="Chicken Tikka"
    cuisine="South Indian"
    rating="4.4"
    cost="599"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights

        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order5', methods=['POST'])
def order5():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="South Indian Meals"
    cuisine="South Indian"
    rating="4.4"
    cost="799"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights
        #
        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order6', methods=['POST'])
def order6():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="Shahi Paneer"
    cuisine="Thai"
    rating="4.4"
    cost="900"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights
        #
        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

@app.route('/order7', methods=['POST'])
def order7():
    global food_name,cuisine,rating,cost
    # localhost_addr="https://localhost:5000"

    db=mysql.connector.connect(
        host="localhost",
        user='root',
        password='lsk12312',
        database='wanderplates'
    )
    mycursor=db.cursor()

    print("check1")
    food_name="Rogan Josh"
    cuisine="Kashmiri"
    rating="4.4"
    cost="777"


    if request.form['click']=='btn_click':
        # TABLE CREATION flights
        #
        time.sleep(3)
        query=(
                "INSERT INTO POPULAR_FOODS(FOOD_NAME,CUISINE,RATING,COST) VALUES('"+food_name+"','"+cuisine+"','"+
                rating+"','"+cost+"')")

        mycursor.execute(query)
        db.commit()

        ticket_booked = """
                                        <html>
                                        <head>
                                        <script>
                                        alert("THANK YOU FOR YOUR ORDER!!!")
                                        </script>
                                        </head>
                                        <body>
                                        </body>
                                        </html>
                                        """

    return render_template_string(ticket_booked)

if __name__=='__main__':
    app.run(debug=True,port=7000)




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
