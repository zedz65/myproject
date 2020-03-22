from flask import render_template, redirect, url_for
from application import app, db
from application.models import Car, Part
from application.forms import CarForm, PartForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 carData = Car.query.all()
 return render_template('home.html', title='Home', cars=carData)


@app.route('/car', methods=['GET', 'POST']) #Get = read Post = Write
def car():
    form = CarForm()
    if form.validate_on_submit():
        carData = Car(
            make = form.make.data,
            model = form.model.data,
            year = form.year.data,
            reg = form.reg.data
        )

        db.session.add(carData)
        db.session.commit()

        return redirect(url_for('parts'))

    else:
        print(form.errors)

    return render_template('car.html', title='car', form=form)




@app.route('/parts', methods=['GET', 'POST'])
def parts():
    form = PartForm()
    if form.validate_on_submit():
        partData = Part(
            parts=form.cars_id.data,
            part_name=form.part_name.data,
            part_desc=form.part_desc.data,
            price=form.price.data           
        )
        db.session.add(partData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('parts.html', title='parts', form=form)

