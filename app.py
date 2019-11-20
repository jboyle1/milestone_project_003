from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/architecture')
def architecture():
    return render_template('architecture.html')


@app.route('/commercial')
def commercial():
    return render_template('commercial.html')


@app.route('/property')
def property():
    return render_template('property.html')


@app.route('/construction')
def construction():
    return render_template('construction.html')


if __name__ == "__main__":
    app.run(debug=True)
