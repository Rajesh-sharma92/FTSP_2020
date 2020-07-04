
from flask import Flask , render_template


app = Flask(__name__)



@app.route("/index")
def hello():
    return render_template("index.html")


@app.route("/bstp")
def boot():
    return render_template("bootstrap.html")


@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap1.html")    





app.run(debug=True)


