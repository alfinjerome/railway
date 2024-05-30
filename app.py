from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('book.html')


@app.route("/trains")
def trainsdetails():
    return render_template('trains.html')


@app.route("/details")
def passdetails():
    return render_template("details.html")


@app.route("/confirmation")
def billdetails():
    return render_template("confirmation.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
