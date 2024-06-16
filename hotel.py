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
# fom app import app

app=Flask(__name__,template_folder='template')
# @app.route('/')
# def index():
#     return render_template('home.html')


@app.route('/hotel')
def hotel():
    return render_template('hotels.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/help')
def help():
    return render_template('help.html')



if __name__=='__main__':
    app.run(debug=True,port=5000)



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
