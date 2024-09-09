from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "<p>This is a Trunk Based Testing Repo https://www.cncglobal.io</p>"

if __name__ == "__main__":
    app.run(debug=True)