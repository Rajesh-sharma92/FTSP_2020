from flask import Flask, request, render_template, url_for
from validator import credit_card

app = Flask(__name__)

@app.route("/main")
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def output():
    form_data = request.form["card"]
    status = credit_card(form_data)
    return render_template("response.html",status=status)

if __name__ == "__main__":
    app.run(debug=True)
