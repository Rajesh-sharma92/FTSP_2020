from flask import Flask,render_template,request,url_for
import json
from age_cal import calc

server = Flask('__name__')

@server.route('/')
def greeting():
    data = {
    'person':'RAJESH SHARMA' ,
    'place':'Jaipur, Rajasthan,India'}
    # return render_template('base.html',val1=data)
    return render_template('inp_form.html')

@server.route('/get_user_info')
def user_data():
    name = request.args.get("name")
    age = request.args.get("age")
    data = {'person':name ,'place':age}
    return render_template('base.html',val1=data)

@server.route('/user/<name>/<age>')
def user_info(name,age):
    data = {'person':name ,'place':age}
    return render_template('base.html',val1=data)

@server.route('/json_data', methods=['POST'])
def user_json():
    name = request.json.get("name")
    age = request.json.get("age")
    data = {'person':name ,'place':age , "returned":True}
    # return render_template('base.html',val1=data)
    return json.dumps(data)

@server.route('/dual', methods=['GET','POST'])
def dual_fun():
    if request.method=='GET':
        name = request.args.get("name")
        age = request.args.get("age")
        data = {'person':name ,'place':age}
        return render_template('base.html',val1=data)
    else:
        name = request.json.get("name")
        age = request.json.get("age")
        data = {'person':name ,'place':age , "returned":False}
        return json.dumps(data)

@server.route('/form_data' , methods=['POST'])
def get_form():
    name = request.form['name']
    age = request.form['age']
    age_group = calc(age)
    data = {'person':name , 'place':age_group}
    return render_template('base.html',val1=data)

if __name__ == '__main__':
    server.run(port=8000 , debug=True)