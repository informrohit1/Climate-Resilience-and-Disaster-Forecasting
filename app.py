from flask import Flask, render_template, request, jsonify
from forms import InputForm
import pandas as pd
import joblib
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

# Load your pre-trained model
model = joblib.load("model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/api/fetch_weather", methods=["GET"])
def fetch_weather():
    """
    Fetch daily forecast data from WeatherAPI, sum hourly precipitation,
    and return location_name so we can show it in the final prediction.
    If sum is 0, set precipitation to 0.001.
    """
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if not lat or not lon:
        return jsonify({"error": "Missing lat or lon"}), 400

    api_key = "bf320090dd5f4c30a67201629242609  "  # <-- Replace with your key
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": f"{lat},{lon}",
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), 400

    data = response.json()
    if "error" in data:
        return jsonify({"error": data["error"]["message"]}), 400

    # Extract location name if available
    location_name = data.get("location", {}).get("name", "this location")

    # Current weather
    current_temp = data["current"]["temp_c"]
    current_humidity = data["current"]["humidity"]
    current_wind_speed = data["current"]["wind_kph"]

    # Sum hourly precipitation
    hour_info = data["forecast"]["forecastday"][0]["hour"]
    precip_sum = sum(h["precip_mm"] for h in hour_info)
    if precip_sum == 0:
        precip_sum = 0.01

    day_info = data["forecast"]["forecastday"][0]["day"]
    max_temp = day_info["maxtemp_c"]
    min_temp = day_info["mintemp_c"]
    uv_index = day_info["uv"]

    return {
        "location_name": location_name,
        "temperature": current_temp,
        "humidity": current_humidity,
        "wind_speed": current_wind_speed,
        "precipitation": round(precip_sum, 3),
        "max_temperature": max_temp,
        "min_temperature": min_temp,
        "uv_index": uv_index
    }

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    message = "Please Provide Valid Input Details!"

    if form.validate_on_submit():
        selected_date = form.date.data
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day

        # Construct input DataFrame
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
            year=[year],
            month=[month],
            day=[day]
        ))

        prediction = model.predict(X_new)[0]

        # Safely handle place_name (avoid NoneType.strip() error)
        raw_place = form.place_name.data  # Could be None
        place_name = (raw_place or "").strip() or "this location"

        if prediction == 0:
            message = f"There is a High chance of DROUGHT in {place_name}"
        elif prediction == 1:
            message = f"There is a High Chance of Earthquake in {place_name}"
        elif prediction == 2:
            message = f"There is a High Chance of Eruption in {place_name}"
        elif prediction == 3:
            message = f"There is a High Chance of Flood in {place_name}"
        elif prediction == 4:
            message = f"There is a High Chance of Hurricane in {place_name}"
        elif prediction == 5:
            message = f"There is a High Chance of Snow Storm in {place_name}"
        elif prediction == 6:
            message = f"There is a High Chance of Tropical Cyclone in {place_name}"
        elif prediction == 7:
            message = f"There is a High Chance of Tornado in {place_name}"
        elif prediction == 8:
            message = f"There is a High Chance of Volcanic Outbreak in {place_name}"
        else:
            message = f"There is a High Chance of Wild Fire in {place_name}"

    return render_template("predict.html", title="Prediction Page", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
