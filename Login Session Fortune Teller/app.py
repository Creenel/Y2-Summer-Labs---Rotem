from flask import Flask, render_template, request, redirect, url_for	
from flask import session as login_session
import random
app = Flask(__name__)
app.config['SECRET_KEY'] = "Atef"

@app.route('/',methods = ["GET", "POST"])
def main():
	if request.method == 'GET':
		return render_template("main.html")
	else:
		login_session['username'] = request.form['username']
		login_session['bm'] = request.form['bm']
		return redirect(url_for('home'))




@app.route('/home')
def home():
	return render_template("home.html",user = login_session['username'], month = login_session['bm'])

@app.route('/fortune', methods = ('GET','POST'))
def fortune():
	fortunes = ["You will have a great day!","A surprise is waiting for you.","Today is your lucky day!","Happiness will find you.","Be cautious today.","You will meet someone special.","An opportunity will arise.","Expect the unexpected.","Good news is coming your way.","You will achieve your goals.","You will be punished."]
	if len(login_session['bm']) <= 9:
		login_session['chosen_fortune']=fortunes[len(login_session['bm'])]
	else:
		login_session['chosen_fortune'] = fortunes[10]
	return render_template('fortune.html',fortune = login_session['chosen_fortune'])

if __name__ == '__main__':
	app.run(debug=True)