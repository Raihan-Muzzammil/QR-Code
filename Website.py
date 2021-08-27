from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)
@app.route("/")
def home():
    return (render_template("index.html"))

@app.route("/home")
def home1():
    return (render_template("index.html"))

@app.route("/generate")
def gen():
    return (render_template("Generator.html"))

@app.route("/random")
def rand():
    return (render_template("HTML.html"))

@app.route("/random")
def rand():
    return (render_template("HTML.html"))

if __name__ == "__main__" :
    app.run(debug=True)