from flask import Flask, render_template, request
app = Flask('app')


@app.route('/')
def form():
  return render_template("index.html")

@app.route("/form.html")
def lien_form():
  return render_template("form.html")

@app.route("/traitement", methods=["POST"])
def resultat():
  r11 = request.form["q11"]
  r12 = request.form["q12"]
  r13 = request.form["q13"]

  return render_template("finform.html", r11=r11, r12=r12, r13=r13)


app.run(host='0.0.0.0', port=8080)