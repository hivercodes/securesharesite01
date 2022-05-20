from flask import Flask, render_template, url_for, request, redirect, send_file, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField, TextAreaField, FileField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asgthasdfDsfesfsdfdgzs!!!#tJAJKMNJKy46yu357du35ud3t5rysdfau56ud5e'
Bootstrap(app)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login")
def home():
    return render_template("login.html")

@app.route("/register")
def home():
    return render_template("register.html")






















if __name__ == "__main__":
    app.run(debug=True)
