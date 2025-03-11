from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello 温桓瑄!"
@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"
@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))


if __name__ == "__main__":
    app.run()