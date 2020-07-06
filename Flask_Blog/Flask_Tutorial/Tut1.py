
from flask import Flask , render_template


app = Flask(__name__)



@app.route("/")
@app.route("/home")
def hello():
    return render_template("index.html")



@app.route("/about")
def Rajesh():
    name = "Rajesh sharma"
    return render_template("about.html" , name=name)



app.run(debug=True)




