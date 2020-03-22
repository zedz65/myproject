from application import db

class Car(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reg = db.Column(db.String(7), nullable=False, unique=True)
    #parts = db.relationship('Part', back_populates='car.car_id')
    parts = db.relationship('Part', backref='cars_id', lazy=True)

    def __repr__(self):
        return ''.join([
            'Car: ', self.make, ' ', self.model, '\r\n',
            'Year: ', self.year, '\r\n', self.reg
            ])



class Part(db.Model):
    part_id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(500), nullable=False)
    part_desc = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cars_id = db.Column(db.Integer, db.ForeignKey('car.car_id'), nullable=False)
    #car = db.relationship('Car', back_populates='parts')


    def __repr__(self):
        return ''.join([
            'Part: ', self.part_name, ' ', self.part_desc, '\r\n',
            'Car_id: ', self.cars_id, '\r\n', self.price
            ])

