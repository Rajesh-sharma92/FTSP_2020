from flask import Flask
app = Flask('__name__')

@app.route('/')
@app.route('/home')
def home():
	return "<h1> Hello Guys, Welcome to Forsk Coding School and Thanks to Mr. Corey Schafer YouTuber Guy, WOW ..... </h1>"

@app.route('/About')
def display():
	return "<h3> This is About Page!! , Hey All of You Guys and It's Good Channel for Tech Guys !!! <h3>"

if __name__ == '__main__':
	app.run(debug=True)

