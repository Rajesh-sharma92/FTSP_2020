from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def Pattern():
    # return '<h1>This is the Test Page for My First Website.</h1>'
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
