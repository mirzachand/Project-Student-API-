from werkzeug.wrappers import request, Response
from flask import Flask, jsonify, request
from students import getstevedetails, getmirzadetails, getAllendetails, getkarthikeyadetails, getrobertdetails, getHarrysonWellsdetails

app = Flask(__name__)

@app.route('/steve', methods = ['GET', 'POST'])
def steve():
    if(request.method == 'GET'):
        return getstevedetails()


@app.route('/mirza', methods = ['GET', 'POST'])
def mirza():
    if(request.method == 'GET'):
        return getmirzadetails()

@app.route('/Allen', methods = ['GET', 'POST'])
def Allen():
    if(request.method == 'GET'):
        return getAllendetails()


@app.route('/karthikeya', methods = ['GET', 'POST'])
def karthikeya():
    if(request.method == 'GET'):
        return getkarthikeyadetails()


@app.route('/robert', methods = ['GET', 'POST'])
def robert():
    if(request.method == 'GET'):
        return getrobertdetails()

@app.route('/HarrysonWells', methods = ['GET', 'POST'])
def HarrysonWells():
    if(request.method == 'GET'):
        return getHarrysonWellsdetails()



if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 9000, app)