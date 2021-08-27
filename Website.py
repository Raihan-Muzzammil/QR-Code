from QR import qrgen
from flask import Flask, render_template, request, send_file
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Generator.html")


@app.route("/generator", methods=["POST"])
def generate():
    global tex
    tex = request.form["qr"]
    return render_template("Download.html")


@app.route("/download")
def gen():
    qrgen(tex)
    filename = tex + '.png'
    return send_file(filename, as_attachment=True)


@app.route("/random")
def rand():
    return render_template("HTML.html")


if __name__ == "__main__":
    app.run(debug=True)
