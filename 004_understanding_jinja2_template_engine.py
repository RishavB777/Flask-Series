## Jinja2 template engine
"""
{%...%} for loops, if statements
{{  }} expressions to print values from other sources
{#...#} comments

"""
from flask import Flask,redirect,url_for,render_template,request



app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/form')
def form():
    return render_template('submit.html')

@app.route('/submit',methods=['POST','GET'])

def submit():
    avg_score = 0
    if request.method=="POST":
        science=float(request.form['science']) 
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        avg_score=(science+maths+c+data_science)/4

    """if avg_score>=50:
        res = "success"
    else:
        res = "fail" """

    return render_template("jinja.html",score=avg_score)


if __name__=="__main__":
    app.run(debug=True)