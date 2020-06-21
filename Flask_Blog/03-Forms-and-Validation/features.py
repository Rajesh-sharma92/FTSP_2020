from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm, LoginForm

app = Flask('__name__')

app.config['SECRET_KEY'] = 'aa3cb1e90591942a6b010b8ea9421803'

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

@app.route('/register', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data} !!!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html' , title='Register' , form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)

