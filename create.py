from application import db
from application.models import Car

db.drop_all()
db.create_all()