from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = mongodb+srv: // root: IbwjWiiKm4xaT2Jn@cluster0-hgg7x.mongodb.net/test?retryWrites = true & w = majority
mongo = PyMongo(app)


@app.route('/')
def index():
    return '''
        <from method="POST" action="/create" enctype="multipart/form-data">
            <input type="text" name="property">
            <input type="file" name="property_image">
            <input type="submit">
    '''
