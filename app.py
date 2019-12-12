from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from datetime import datetime
import os

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Boyle:jeddy1234@paddy-photodb-o2y1x.mongodb.net/paddy_photodb?retryWrites=true&w=majority'
mongo = PyMongo(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


##Homepage routing

@app.route('/')
def index():
    return render_template('index.html', paddy_photodb=mongo.db.catagory_photos.find())


##Catagory routing

@app.route('/architecture')
def architecture():
    return render_template('architecture.html', paddy_photodb=mongo.db.photos.find())


@app.route('/commercial')
def commercial():
    return render_template('commercial.html', paddy_photodb=mongo.db.photos_002.find())


@app.route('/property')
def property():
    return render_template('property.html', paddy_photodb=mongo.db.photos_003.find())


@app.route('/construction')
def construction():
    return render_template('construction.html', paddy_photodb=mongo.db.photos_004.find())


##Testimonial routing

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/testimonials', methods=['POST', 'GET'])
def testimonials(): 
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/testimonials')
        except:
            return 'There was an issue adding your testimonial'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('testimonials.html', tasks=tasks)



@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/testimonials')
    except:
        return 'There was a problem deleting that testimonial'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/testimonials')
        except:
            return 'There was an issue updating your testimonial'

    else:
        return render_template('update.html', task=task)




##Architecture routing

@app.route('/st-pauls-church')
def st_pauls_church():
    return render_template('st-pauls-church.html', paddy_photodb=mongo.db.st_pauls_curch.find())

@app.route('/lutyens-house')
def lutyens_house():
    return render_template('lutyens-house.html', paddy_photodb=mongo.db.lutyens_house.find())

@app.route('/sun-lounge')
def sun_lounge():
    return render_template('sun-lounge.html', paddy_photodb=mongo.db.sun_lounge.find())

@app.route('/somerset-house')
def somerset_house():
    return render_template('somerset-house.html', paddy_photodb=mongo.db.somerset_house.find())

@app.route('/plascoch')
def plascoch():
    return render_template('plascoch.html', paddy_photodb=mongo.db.plascoch.find())

@app.route('/hawthorns')
def hawthorns():
    return render_template('hawthorns.html', paddy_photodb=mongo.db.hawthorns.find())

@app.route('/hastings-college')
def hastings_college():
    return render_template('hastings-college.html', paddy_photodb=mongo.db.hastings_college.find())

@app.route('/hamstone-house')
def hamstone_house():
    return render_template('hamstone-house.html', paddy_photodb=mongo.db.hamstone_house.find())

@app.route('/copyhold-barn')
def copyhold_barn():
    return render_template('copyhold-barn.html', paddy_photodb=mongo.db.copyhold_barn.find())

##Commercial routing

@app.route('/padstone')
def padstone():
    return render_template('padstone.html', paddy_photodb=mongo.db.padstone.find())

@app.route('/woodbase')
def woodbase():
    return render_template('woodbase.html', paddy_photodb=mongo.db.woodbase.find())

@app.route('/various')
def various():
    return render_template('various.html', paddy_photodb=mongo.db.various.find())

@app.route('/emess')
def emess():
    return render_template('emess.html', paddy_photodb=mongo.db.emess.find())

@app.route('/fox')
def fox():
    return render_template('fox.html', paddy_photodb=mongo.db.fox.find())

@app.route('/manoukian')
def manoukian():
    return render_template('manoukian.html', paddy_photodb=mongo.db.manoukian.find())

##Property routing

@app.route('/ash')
def ash():
    return render_template('ash.html', paddy_photodb=mongo.db.ash.find())

@app.route('/beachaven')
def beachaven():
    return render_template('beachaven.html', paddy_photodb=mongo.db.beachaven.find())

@app.route('/etham')
def etham():
    return render_template('etham.html', paddy_photodb=mongo.db.etham.find())

@app.route('/garden')
def garden():
    return render_template('garden.html', paddy_photodb=mongo.db.garden.find())

@app.route('/marina')
def marina():
    return render_template('marina.html', paddy_photodb=mongo.db.marina.find())

@app.route('/markwich')
def markwich():
    return render_template('markwich.html', paddy_photodb=mongo.db.markwich.find())

@app.route('/pages')
def pages():
    return render_template('pages.html', paddy_photodb=mongo.db.pages.find())

@app.route('/chapel')
def chapel():
    return render_template('chapel.html', paddy_photodb=mongo.db.chapel.find())

@app.route('/street')
def street():
    return render_template('street.html', paddy_photodb=mongo.db.street.find())


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)