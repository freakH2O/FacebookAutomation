from flask import Flask, render_template, request,redirect
from flask_pymongo import PyMongo
from waitress import serve
import os
started=[]
app = Flask(__name__)


app.config['MONGO_DBNAME']='users'
app.config['MONGO_URI']='mongodb://hamza:gogoville123@ds157064.mlab.com:57064/users'
app.inta = 1
app.dic=[]
mongo=PyMongo(app)

@app.route('/',methods={'POST','GET'})
def main():
    return "Hello"
    


if __name__ == '__main__':
    from waitress import serve

    serve(app, host='0.0.0.0', port=8080)
    #serve(app, listen='*:8080')
    app.run(debug=True ,port=8080)
