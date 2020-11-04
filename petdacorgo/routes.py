from flask import render_template, url_for, flash, redirect, request
from petdacorgo import app, db, bcrypt
from petdacorgo.forms import RegistrationForm, LoginForm
from petdacorgo.models import User, Pet
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/friends")
def friends():
    pets = Pet.query.all()
    return render_template('friends.html', title = 'Our Friends', pets=pets)

@app.route("/friends/<int:pet_id>")
def friend(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template('pet.html', 
        title=pet.petname, 
        petname=pet.petname, 
        fullname=pet.fullname, 
        profile_picture=pet.profile_picture,
        birthday=pet.birthday, 
        weight=pet.weight, 
        info=pet.info,
        photoset1=[pet.photo1, pet.photo2, pet.photo3],
        photoset2=[pet.photo4, pet.photo5]
    )

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))