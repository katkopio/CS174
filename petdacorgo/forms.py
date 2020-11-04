from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from petdacorgo.models import User, Pet
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    contact_num = StringField('Contact Number', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddFriendForm(FlaskForm):
    petname = StringField('Pet Name', validators=[DataRequired()])
    fullname = StringField('Full Name', validators=[DataRequired()])
    profile_picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    birthday = DateField('Birthday', validators=[DataRequired()])
    weight = StringField('Weight', validators=[DataRequired()])
    info  = TextAreaField('Pet Description')
    photo1 = FileField('Photo #1', validators=[FileAllowed(['jpg', 'png'])])
    photo2 = FileField('Photo #2', validators=[FileAllowed(['jpg', 'png'])])
    photo3 = FileField('Photo #3', validators=[FileAllowed(['jpg', 'png'])])
    photo4 = FileField('Photo #4', validators=[FileAllowed(['jpg', 'png'])])
    photo5 = FileField('Photo #5', validators=[FileAllowed(['jpg', 'png'])])
    pet_type = SelectField('Pet Type', choices=[('cat', 'Cat'), ('dog', 'Dog')])
    submit = SubmitField('Add Friend')
