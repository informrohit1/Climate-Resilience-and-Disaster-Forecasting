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

X_data = pd.read_csv("notebooks\dataCleaning\data.csv")

class InputForm(FlaskForm):
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
    year = IntegerField(
        label='Year',
        validators =[DataRequired()]
    )
    month = IntegerField(
        label='Month',
        validators =[DataRequired(),NumberRange(min=1, max=12, message="Month must be between 1 and 12")
        ]
    )
    day = IntegerField(
        label='Day',
        validators =[DataRequired(),NumberRange(min=1, max=31, message="day must be between 1 and 31")
        ]
    )

    
    submit = SubmitField('Submit')
