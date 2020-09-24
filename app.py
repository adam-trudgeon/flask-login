#import the Flask class from flask
from flask import Flask, render_template, redirect, url_for, request


#create the application object
app = Flask(__name__)

#use decorators to link the function to a url
@app.route('/')
def home():
    return "Welcome to Post It Fo' Life" #returns a string
   0
@app.route('/welcome')
def welcome():
    return render_template('welcome.html') # render a template
    
#route for handling the login page logic
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else: 
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
    
#start the server with run()
if __name__ == '__main__':
    app.run(debug=True)