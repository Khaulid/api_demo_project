"""

#HassanWeatherAPIProject 
#8/24 

#ETL data pipeline for API weather data 

"""

import requests
import pandas as pd
import os

# ========== CONFIG ==========
base_url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("API_KEY") # Replace with your actual key
output_file = os.path.join(os.getcwd(), "weather_data.csv")  # Absolute path for clarity
# ============================

# Extract
def extract_data(city):
    try:
        print(f"[INFO] Extracting data for city: {city}")
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:  # API-level error
            print(f"[ERROR] API error for {city}: {data.get('message')}")
            return None

        return data
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed for {city}: {e}")
        return None

# Transform
def transform_weather(data):
    try:
        print("[INFO] Transforming data...")
        return {
            "city": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "description": data.get("weather", [{}])[0].get("description")
        }
    except Exception as e:
        print(f"[ERROR] Transformation failed: {e}")
        return None

# Load
def load_data(data, filename):
    try:
        print(f"[INFO] Loading data to {filename}...")
        df = pd.DataFrame([data])
        df.to_csv(filename, index=False)
        print(f"[SUCCESS] Data saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to save CSV: {e}")

# Run ETL
def run_etl_pipeline(city):
    data = extract_data(city)
    if not data:
        print("[ERROR] Extraction failed, stopping pipeline.")
        return

    transformed = transform_weather(data)
    if not transformed:
        print("[ERROR] Transformation failed, stopping pipeline.")
        return

    load_data(transformed, output_file)

# ====== EXECUTE ======
if __name__ == "__main__":
    city = "Indianapolis"  # Change as needed
    run_etl_pipeline(city)
                 









