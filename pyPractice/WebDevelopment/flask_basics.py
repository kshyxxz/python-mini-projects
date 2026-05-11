from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/greet/<name>')
def greet(name):
	return render_template('greet.html', name=name)

@app.errorhandler(404)
def err(error):
	return render_template('pagenotfound404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)