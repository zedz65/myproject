from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Datarequired, Length, ValidationError

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