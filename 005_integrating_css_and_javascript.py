from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('submitcss.html')

@app.route('/submit',methods=["POST","GET"])
def submit():
    if request.method=="POST":
        avg = (float(request.form['science'])+float(request.form['c'])+float(request.form['datascience'])+float(request.form['maths']))/4
    if avg > 30:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template("resultjs.html",result=res,marks=avg)

if __name__ == "__main__":
    app.run(debug=True)
