from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Boyle:jeddy1234@paddy-photodb-o2y1x.mongodb.net/paddy_photodb?retryWrites=true&w=majority'
mongo = PyMongo(app)

##Homepage routing

@app.route('/')
def index():
    return render_template('index.html', paddy_photodb=mongo.db.catagory_photos.find())


@app.route('/architecture')
def architecture():
    return render_template('architecture.html', paddy_photodb=mongo.db.photos.find())


@app.route('/commercial')
def commercial():
    return render_template('commercial.html')


@app.route('/property')
def property():
    return render_template('property.html')


@app.route('/construction')
def construction():
    return render_template('construction.html')



##Architecture routing

@app.route('/st-pauls-church')
def st_pauls_church():
    return render_template('st-pauls-church.html')







@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(debug=True)
