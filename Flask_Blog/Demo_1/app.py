from flask import Flask,render_template,request

app = Flask('__name__')

@app.route('/')
def greeting():
    data = {
    'person':'RAJESH SHARMA' ,
    'place':'Jaipur, Rajasthan,India'}
    return render_template('base.html',val1=data)


@app.route('/get_user_info')
def user_data():
    name = request.args.get("name")
    age = request.args.get("age")
    data = {'person':name ,'place':age}
    return render_template('base.html',val1=data)

@app.route('/user/<name>/<age>')
def user_info(name,age):
    data = {'person':name ,'place':age}
    return render_template('base.html',val1=data)


@app.route('/home')
@app.route('/hello/msg')
def home():
    return '<h1> Hello Everyone, Welcome to the FORSK CODING SCHOOL. </h1>'

@app.route('/home/text')
def demo():
    return '<h4> Hey Guys!!! , Hello World. </h4>'

@app.route('/testing')
def testing():
    return '<h4> Hey Folks!!! , Hello India People. </h4>'


if __name__ == '__main__':
    app.run(port=8000 , debug=True)
