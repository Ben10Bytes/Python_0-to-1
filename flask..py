# flask is lightwweight
from flask import Flask
app=Flask(__name__) # __name__ is located to static file,database etc...to flask
# the working of routing is mapping o, working like a WSGI
@app.route('/')
def hello_world():
    return"hello"
@app.route('/about')
def about():
    return "about us"
if __name__ == '__main__':
    app.run(debug=True)




