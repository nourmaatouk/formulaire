from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template("index.html")

@app.route("/heure")
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    print(h, m, s)
    return render_template("heure.html", heure=h, minute=m, seconde=s)

@app.route("/eleves")
def eleves():
    return render_template("eleves.htmls")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ =='__main__':
    app.run(debug=True)
           

