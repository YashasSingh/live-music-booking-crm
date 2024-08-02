from flask import Flask, request, redirect, render_template, url_for
import csv
import os
from dotenv import load_dotenv
RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')
RECAPTCHA_SITE_KEY= os.getenv('RECAPTCHA_SITE_KEY')
import requests

app = Flask(__name__)

def check_credentials(username, password):
    with open('users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        card_number = request.form['card_number']
        address = request.form['address']
        
        # Here you can add code to process and store the data,
        # e.g., save to a database or a file
        # For example, saving to a CSV file or a database

        return "Signup successful!"

    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    recaptcha_response = request.form['g-recaptcha-response']
    
    # Verify reCAPTCHA
    

    if check_credentials(username, password):
        return redirect(url_for('dashboard'))
    else:
        return "Login failed. Please check your credentials."


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return "Welcome to the Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
