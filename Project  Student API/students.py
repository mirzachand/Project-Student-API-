from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson.json_util import dumps


def getstevedetails():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Netzwerk']
    collection = db['steve']
    students = collection.find()
    return dumps(students)

def getmirzadetails():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Netzwerk']
    collection = db['mirza']
    students = collection.find()
    return dumps(students)

def getAllendetails():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Netzwerk']
    collection = db['Allen']
    students = collection.find()
    return dumps(students)

def getkarthikeyadetails():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Netzwerk']
    collection = db['karthikeya']
    students = collection.find()
    return dumps(students)

def getrobertdetails():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Netzwerk']
    collection = db['robert']
    students = collection.find()
    return dumps(students)

def getHarrysonWellsdetails():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Netzwerk']
    collection = db['HarrysonWells']
    students = collection.find()
    return dumps(students)

