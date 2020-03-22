from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, ValidationError
from application.models import Car, Part

class CarForm(FlaskForm):
    make = StringField('Enter Make',
        validators = [
            DataRequired(),
            Length(min=3, max=30)
        ]
    )
    model = StringField('Enter Model',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    year = StringField('Enter Year',
        validators = [
            DataRequired(),
            Length(min=4, max=4)
        ]
    )
    reg = StringField('Enter Registration',
        validators = [
            DataRequired(),
            Length(min=2, max=7)
        ]
    )
    submit = SubmitField('Submit')






#Form for Parts
class PartForm(FlaskForm):


    cars_id = QuerySelectField('Car ID',
    query_factory=lambda: Car.query.all(),
    allow_blank=False)


    part_name = StringField('Part Name',
        validators = [
            DataRequired(),
            Length(min=2, max=500)
        ]
    )
    part_desc = StringField('Part Description',
        validators = [
            DataRequired(),
            Length(min=2, max=500)
        ]
    )
    price = StringField('Price',
        validators = [
            DataRequired(),
            Length(min=1, max=7)
        ]
    )

    
    submit = SubmitField('Submit')