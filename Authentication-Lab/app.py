from collections.abc import MutableMapping

from flask import Flask, render_template,request, redirect, url_for
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
	login_session['quotes'] = []
	if request.method == "POST":
		login_session['user'] = auth.create_user_with_email_and_password(request.form['email_address'],request.form['password'])
		return redirect(url_for("home"))
	else:
		return render_template("signup.html")



@app.route('/signin', methods = ['GET','POST'])
def signin():
	if request.method == "POST":
		login_session['user'] = auth.sign_in_with_email_and_password(request.form['email_address'], request.form['password'])
		return redirect(url_for("home"))
	else:
		return render_template("signin.html")

@app.route('/home', methods = ['GET','POST'])
def home():
	print(request.method)
	if request.method == 'POST':
		quote = request.form['quoteinp']
		print(quote)
		login_session['quotes'].append(quote)
		login_session.modified = True
		return redirect(url_for('thanks'))
	else:
		return render_template("home.html")

@app.route('/display')
def display():
	print(login_session['quotes'])
	return render_template("display.html",quotes = login_session['quotes'])

@app.route('/thanks', methods = ['GET','POST'])
def thanks():
	print(login_session['quotes'])
	return render_template("thanks.html", quotes = login_session['quotes'])

@app.route('/signout')
def signout():
	print("test")
	login_session['user'] = None
	auth.current_user = None
	return redirect(url_for("signin"))







if __name__ == '__main__':
	app.run(debug = True)

