from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("name_form.html")

@app.route("/submit_name", methods=["POST"])
def submit_name():
    name = request.form.get("name")
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
