from application import db

class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reg = db.Column(db.String(7), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Car: ', self.make, ' ', self.model, '\r\n',
            'Year: ', self.year, '\r\n', self.reg
            ])

