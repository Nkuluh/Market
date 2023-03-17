from flask import Flask, render_template

app = Flask(__name__)

Vegs= [
  {'id': 1,
  'name': 'Tomato',
  'price per kg': 'R20'},
  {'id': 2,
  'name': 'Cabbage',
  'price per kg': 'R30'},
  {'id': 3,
  'name': 'carrot',
  'price per kg': 'R22'},
  {'id': 4,
  'name': 'pepper',
  'price per kg': 'R15'},
]

@app.route("/")
def hello():
    return render_template('home.html', vegs=Vegs)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)