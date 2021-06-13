### BUILDING URL DYNAMICALLY
# Variable rules and URL building
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return("Welcome to our Flask app")
@app.route('/success/<int:score>')
# <> will help us pass parameters from our URL to the function
# By default <> will take string datatype
# So we need to provide the datatype using /<datatype:variable>
def success(score):
    return "The person has passed and marks "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and marks "+str(score)
## What if we want to redirect the user to different pages for
# different conditions and not show the outcome in the same page

@app.route('/results/<int:score>')
def results(score):
    if score<=30:
        result = "fail"
    else:
        result =  "success"
    return redirect(url_for(result,score=score))
    #url_for() takes two parameters
    # One is the url of the page
    # Second is the parameter that URL takes
if __name__=='__main__':
    app.run(debug=True)