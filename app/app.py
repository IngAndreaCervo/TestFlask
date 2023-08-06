from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    wow ="beautiful"
    return render_template("index.html")

@app.route("/info/")
def info():
    return f"<h2> Queste sono un sacco di informazioni </h2>"

@app.route("/info/<name>")
def nome_ok(name):
    return f"<h2> Il mio nome: {name} </h2>"

@app.route("/info-errore/<name>")
def errore(name):
    return f"<h2> Generiamo un errore </h2>".format(name[50])



if __name__ == "__main__":
    app.run(debug=True)