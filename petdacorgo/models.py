from petdacorgo import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contact_num = db.Column(db.String(20), unique=True, nullable=False)

    def get_id(self):
           return (self.user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Pet(db.Model):
    pet_id = db.Column(db.Integer, primary_key=True)
    petname = db.Column(db.String(10), unique=True, nullable=False)
    fullname = db.Column(db.String(10), unique=False, nullable=False)
    profile_picture = db.Column(db.String(60), unique=False, nullable=False)
    birthday = db.Column(db.String(20), unique=False, nullable=False)
    weight = db.Column(db.String(10), unique=False, nullable=False)
    info = db.Column(db.String(500), unique=False, nullable=False)
    photo1 = db.Column(db.String(120), unique=False, nullable=False)
    photo2 = db.Column(db.String(120), unique=False, nullable=False)
    photo3 = db.Column(db.String(120), unique=False, nullable=False)
    photo4 = db.Column(db.String(120), unique=False, nullable=False)
    photo5 = db.Column(db.String(120), unique=False, nullable=False)
    pet_type = db.Column(db.String(10), unique=False, nullable=False)
    
    def __repr__(self):
        return f"Pet('{self.petname}')"