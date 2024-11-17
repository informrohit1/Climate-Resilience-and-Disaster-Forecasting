import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField,
    FloatField,
)
from wtforms.validators import DataRequired,NumberRange

X_data = pd.read_csv("notebooks/data.csv")

class InputForm(FlaskForm):
    date = DateField(
        label="Select Date",
        validators=[DataRequired()],
        format="%Y-%m-%d",  # Ensure the date format is consistent
        render_kw={"class": "form-control"}
    )
    latitude = FloatField(  
        label='Latitude',
        validators =[DataRequired()] 
    )
    longitude = FloatField(  
        label='Longitude',
        validators =[DataRequired()] 
    )
    temperature = FloatField(
        label='Temperature',
        validators =[DataRequired()]
    )
    max_temperature = FloatField(
        label='Max Temperature',
        validators =[DataRequired()]
    )
    min_temperature = FloatField(
        label='Min Temperature',
        validators =[DataRequired()]
    )
    humidity = FloatField(
        label='Humidity',
        validators =[DataRequired()]
    )
    wind_speed = FloatField(
        label='Wind Speed',
        validators =[DataRequired()]
    )
    precipitation = FloatField(
        label='Precipitation',
        validators =[DataRequired()]
    )
    uv_index = FloatField(
        label='UV Index',
        validators =[DataRequired()]
    )

    
    # year = IntegerField(
    #     label='Year',
    #     validators =[DataRequired()]
    # )
    

    
    submit = SubmitField('Submit')
