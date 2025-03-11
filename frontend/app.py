from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    value = None
    if request.method == "POST":
        value = request.form.get("user_input")
    return render_template("index.html", value=value)

if __name__ == "__main__":
    app.run(debug=True)
