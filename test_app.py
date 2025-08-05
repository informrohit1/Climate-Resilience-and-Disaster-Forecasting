from app import app 

def test_predict():
    with app.test_client() as client:
        response = client.get("/predict")
        assert response.status_code == 200
        assert b"Please Provide Valid Input Details!" in response.data

        # Simulate form submission with valid data
        data = {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "temperature": 22.5,
            "max_temperature": 25.0,
            "min_temperature": 20.0,
            "humidity": 60,
            "wind_speed": 5.0,
            "precipitation": 0.0,
            "uv_index": 3,
            "date": "2023-10-01"
        }
        response = client.post("/predict", data=data)
        assert response.status_code == 200
        assert b"Prediction Result" in response.data

    