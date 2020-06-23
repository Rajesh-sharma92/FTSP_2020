from flask import Flask, request, render_template, url_for
from validator import mobile_no

app = Flask('__name__')

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def output():
    form_data = request.form["Mobile"]
    status = mobile_no(form_data)
    return render_template("response.html",status=status)


@app.route('/about')
def about():
    return '<h1> Our motive is that to repair the Mobile & Checking status of it. <h1>'

if __name__ == '__main__':
    app.run(debug=True)
