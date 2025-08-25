# 🌦 Weather ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline built in Python to fetch real-time weather data from the [OpenWeather API](https://openweathermap.org/api), transform the data, and load it into a CSV file.

---

## 📌 Project Overview
This project demonstrates a basic ETL workflow:
1. **Extract**: Retrieve weather data from OpenWeather API for a given city.
2. **Transform**: Parse the JSON response to extract useful information (e.g., city, temperature, weather description).
3. **Load**: Store the transformed data in a CSV file (`weather_data.csv`).
