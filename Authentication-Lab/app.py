from flask import Flask, render_template,request
from flask import session as login_session
import pyrebase

Config = {
  "apiKey": "AIzaSyBNt2QMiufgrTxM4K-3Gn2kULa7Qq1ANFY",
  "authDomain": "my-quoteboard.firebaseapp.com",
  "projectId": "my-quoteboard",
  "storageBucket": "my-quoteboard.appspot.com",
  "messagingSenderId": "893507159975",
  "appId": "1:893507159975:web:73a5e84692fcf8c32bd882",
  "measurementId": "G-707D0T2RZJ",
  "databaseURL": ""
}

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.config['SECRET_KEY'] = 'starkistspicytuna'

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()



@app.route('/', methods = ["GET","POST"])
def main():
	return render_template("signup.html")
	if method == "POST":
		login_session['user'] = auth.create_user_with_email_and_password(email_address,password)
		login_session['quotes'] = []


@app.route('/signin')
def signin():
	return render_template("signin.html")

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/display')
def display():
	return render_template("display.html")

@app.route('/thanks')
def thanks():
	return render_template("thanks.html")





if __name__ == '__main__':
	app.run(debug = True)

