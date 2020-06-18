from flask import Flask , render_template
app = Flask('__name__')

posts = [
{

	'author' : 'Rajesh sharma',
	'title' : 'Blog post 1',
	'content' : 'first post content',
	'date_posted' : 'June 18, 2020'
},

{

	'author' : 'Jane Doe',
	'title' : 'Blog post 2',
	'content' : 'second post content',
	'date_posted' : 'June 19, 2020'
}

]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html' , posts=posts)


@app.route('/about')
def about():
	return render_template('about.html' , title='about')


if __name__ == '__main__':
	app.run(debug=True)

