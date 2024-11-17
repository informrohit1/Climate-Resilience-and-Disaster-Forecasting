from flask import Flask, url_for,render_template,request
from forms import InputForm 
import pandas as pd
import joblib
import sklearn

app = Flask(__name__)
app.config['SECRET_KEY'] ="secret_key"

model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        # Extract selected date
        selected_date = form.date.data
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day

        X_new = pd.DataFrame(dict(
            latitude=[form.latitude.data],
            longitude=[form.longitude.data],
            temperature=[form.temperature.data],
            max_temperature=[form.max_temperature.data],
            min_temperatude=[form.min_temperature.data],
            humidity=[form.humidity.data],
            wind_speed=[form.wind_speed.data],
            precipitation=[form.precipitation.data],
            uv_index=[form.uv_index.data],
            year=[year],  # Use extracted year
            month=[month],  # Use extracted month
            day=[day]  # Use extracted day
        ))

        prediction = model.predict(X_new)[0]
        if prediction == 0:
            message = "Their is High chance of DROUGHT"
        elif prediction == 1:
            message = "Their is High Chance of EarthQuake"
        elif prediction == 2:
            message = "Their is High Chance of Eruption"
        elif prediction == 3:
            message = "Their is High Chance of Flood"
        elif prediction == 4:
            message = "Their is High Chance of Hurricane"
        elif prediction == 5:
            message = "Their is High Chance of Snow Storm"
        elif prediction == 6:
            message = "Their is High Chance of Tropical Cyclone"
        elif prediction == 7:
            message = "Their is High Chance of Tornado"
        elif prediction == 8:
            message = "Their is High Chance of Volcanic Outbreak"
        else:
            message = "Their is High Chance of Wild Fire"

    else:
        message = "Please Provide Valid Input Details!"

    return render_template("predict.html", title="Prediction Page",form=form, output=message)



if __name__ == "__main__":
    app.run(debug=True)