from flask import Flask
### Creates a WSGI application
# WSGI is a standard protocol we follow while communication between our web server
# and web application takes place
app = Flask(__name__)
# Initializing the Flask object will tell the Flask app to follow the 
# WSGI protocol while communicating with the server

@app.route('/') # This decorator usually takes two parameters, rule and options
# The rule parameter takes a string which will specify the URL that I am going to visit
# in that specific webpage
def welcome():
    return "Welcome to the FLASK"
@app.route('/members')
def members():
    return "Welcome to the FLASK members page"
# When we define a function beneath a decorator then that function will automatically
# Get triggered whenever we are visiting the URL mentioned in the 'rule' parameter
# of the deorator

if __name__ == '__main__':
    app.run(debug=True)