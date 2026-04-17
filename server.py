
# Importing
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
import os
import pickle

app = Flask (__name__)
app.config ['SECRET_KEY'] = os.getenv ('SECRET_KEY')

class Form (FlaskForm):
    height = FloatField ('Height', validators= [DataRequired ()])
    weight = FloatField ('Weight', validators= [DataRequired ()])
    age = FloatField ('Age', validators= [DataRequired ()])
    submit = SubmitField ('Predict')

# Load the model
with open ('./model/gender_detection_model.pkl', 'rb') as f:
    model = pickle.load (f)

@app.route ('/', methods= ['GET', 'POST'])
def home ():
    form = Form ()
    if form.validate_on_submit ():
        height = form.height.data
        weight = form.weight.data
        age = form.age.data
        # Make a prediction
        predict_gender = model.predict ([[height, weight, age]]) [0]
        if predict_gender == 0:
            prediction = "Female"
        else:
            prediction = "Male"

        return render_template ('index.html', form=form, prediction= prediction)
    return render_template ('index.html', form=form)


if __name__ == "__main__":
    app.run (host="0.0.0.0", port=10000)