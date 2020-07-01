from flask import Flask 

app = Flask(__name__)

@app.route("/home")
def home():
	return " <h1> This is Basic Home Page for You guys!!, We have developed Now !! </h1>"


@app.route("/about")
def about():
	return "<p> This is Just a Simple Paragraph Guys!!!, You can enjoy it by Seeing & reading it </p>"

if __name__ == '__main__':
	app.run(debug=True)





