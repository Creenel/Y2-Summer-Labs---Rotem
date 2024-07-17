from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/home')
def home():
	return render_template("home.html")

@app.route('/fortune')
def fortune():
	fortunes = ["You will have a great day!","A surprise is waiting for you.","Today is your lucky day!","Happiness will find you.","Be cautious today.","You will meet someone special.","An opportunity will arise.","Expect the unexpected.","Good news is coming your way.","You will achieve your goals."]
	num1 = random.randint(0,10)
	chosen_fortune=fortunes[num1]
	return render_template('fortune.html',fortune = chosen_fortune)

if __name__ == '__main__':
	app.run(debug=True)