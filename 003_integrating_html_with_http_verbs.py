### INTEGRATE HTML WITH FLASK
### HTTP VERBS GET AND POST

from flask import Flask,redirect,url_for,render_template,request

# The render_template helps us render HTML files
# If you want to go ahead with render_template then you have to
# create a proper folder structure.
# First create a folder called "templates" and create all the HTML files 
# within that folder

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
# The render_template will go directly to the "templates" folder
# If it doesn't find the mentioned HTML file there,
# It wouldn't run

@app.route('/success/<int:score>')
def success(score):
    return render_template("result.html",result="Passed",marks=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template("result.html",result="Failed",marks=score)

@app.route('/form')
def form():
    return render_template('submit.html')

@app.route('/submit',methods=['POST','GET'])
## The second parameter of the 'route()' function is the 'methods'
# where we mention the methods we want to use in this HTML page
def submit():
    avg_score = 0
    if request.method=="POST":
        # request helps us to read the posted values
        science=float(request.form['science']) # Inside the [] provide the id/name
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        avg_score=(science+maths+c+data_science)/4

    if avg_score>=50:
        res = "success"
    else:
        res = "fail"

    return redirect(url_for(res,score=avg_score))


if __name__=="__main__":
    app.run(debug=True)