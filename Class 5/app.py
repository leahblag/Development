from flask import Flask
app = Flask(__name__) # Flask Constructor

# Decorator, a function we can use on a function
@app.route('/') # Decorater, that will take in another function
def hello():
    return 'Hello'

@app.route('/resume')
def my_resume():
    return 'This is my resume! :)'

if __name__ == '__main__':
    app.run()