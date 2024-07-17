from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/home')
def home():
	if request.method == 'GET':
		return render_template("home.html")
	if request.method == 'POST':
		return redirect(url_for('/fortune', month = bm)) 


@app.route('/fortune', methods = ('GET','POST'))
def fortune():
	fortunes = ["You will have a great day!","A surprise is waiting for you.","Today is your lucky day!","Happiness will find you.","Be cautious today.","You will meet someone special.","An opportunity will arise.","Expect the unexpected.","Good news is coming your way.","You will achieve your goals.","You will be punished."]
	if len(request.form['bm']) <= 9:
		chosen_fortune=fortunes[len(request.form['bm'])]
	else:
		chosen_fortune = fortunes[10]
	return render_template('fortune.html',fortune = chosen_fortune)

if __name__ == '__main__':
	app.run(debug=True)