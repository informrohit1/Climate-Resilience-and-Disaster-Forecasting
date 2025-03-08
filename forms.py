import datetime
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    date = DateField(
        label="Today's Date",
        validators=[DataRequired()],
        format="%Y-%m-%d",
        default=datetime.date.today,
        render_kw={"id": "dateField", "readonly": "readonly"}
    )
    latitude = FloatField(
        label='Latitude',
        validators=[DataRequired()],
        render_kw={"id": "latitudeField", "readonly": "readonly"}
    )
    longitude = FloatField(
        label='Longitude',
        validators=[DataRequired()],
        render_kw={"id": "longitudeField", "readonly": "readonly"}
    )
    temperature = FloatField(
        label='Temperature',
        validators=[DataRequired()],
        render_kw={"id": "temperatureField"}
    )
    max_temperature = FloatField(
        label='Max Temperature',
        validators=[DataRequired()],
        render_kw={"id": "maxTempField"}
    )
    min_temperature = FloatField(
        label='Min Temperature',
        validators=[DataRequired()],
        render_kw={"id": "minTempField"}
    )
    humidity = FloatField(
        label='Humidity',
        validators=[DataRequired()],
        render_kw={"id": "humidityField"}
    )
    wind_speed = FloatField(
        label='Wind Speed',
        validators=[DataRequired()],
        render_kw={"id": "windSpeedField"}
    )
    precipitation = FloatField(
        label='Precipitation',
        validators=[DataRequired()],
        render_kw={"id": "precipitationField"}
    )
    uv_index = FloatField(
        label='UV Index',
        validators=[DataRequired()],
        render_kw={"id": "uvIndexField"}
    )

    # Hidden field for place name
    place_name = StringField(
        label='Place Name',
        render_kw={
            "id": "locationNameField",
            "style": "display:none;"
        }
    )

    submit = SubmitField('Submit')
