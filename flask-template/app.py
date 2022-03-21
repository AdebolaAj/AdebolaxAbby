# from flask import Flask
# app = Flask('app')

# @app.route('/')
# def hello_world():
#   return '<h1>Hello, World!</h1>'

# app.run(host='0.0.0.0', port=8080)

from flask import Flask
from flask import render_template
from flask import request
from model import users_capital
app = Flask('app')


# -- Routes section --
@app.route('/results', methods=['GET', 'POST'])
def results():
  if request.method=="POST":
    answers = {"NY": request.form['NYC'], "CA": request.form['Cali'], "MI": request.form['Michigan'], "MD": request.form['Maryland'], "TX": request.form["Texas"]}
    capitalAnswer = users_capital(answers)
    return render_template('result.html', score=capitalAnswer)
    
  else:
   return render_template("result.html", score=capitalAnswer)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)
