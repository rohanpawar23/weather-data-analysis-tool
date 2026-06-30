import numpy as np
import time
from datetime import datetime, timedelta


def generate_data(days=30, seed=None):
    """Generate fake daily temperature (°C) and humidity (%) data."""
    time.sleep(1)
    if seed is not None:
        np.random.seed(seed)

    temp = np.random.normal(loc=20, scale=10, size=days)
    humidity = np.random.normal(loc=60, scale=18, size=days)

    temp = np.clip(temp, -5, 45)
    humidity = np.clip(humidity, 20, 100)

    return temp, humidity


def compute_stats(temp, humidity):
    return {
        "avg_temp": np.average(temp),
        "max_temp": np.max(temp),
        "min_temp": np.min(temp),
        "avg_humidity": np.average(humidity),
    }


def count_extremes(temp, humidity):
    return {
        "hot_days": np.size(temp[temp > 30]),
        "cold_days": np.size(temp[temp < 10]),
        "humid_days": np.size(humidity[humidity > 80]),
    }


def build_month_data(temp, humidity, days=30):
    today = datetime.today().date()
    month_data = {}
    for i in range(days):
        past_date = today - timedelta(days=i)
        month_data[str(past_date)] = {
            "Temperature": float(round(temp[i], 2)),
            "Humidity": float(round(humidity[i], 2)),
        }
    return month_data


def find_hottest_day(month_data):
    return max(month_data.items(), key=lambda item: item[1]["Temperature"])


def print_report(stats, extremes, month_data, hottest):
    print("\nPast 30 Days Weather Report")
    print("-" * 30)
    time.sleep(1)
    print(f"Average temperature: {stats['avg_temp']:.2f}°C")
    print(f"Maximum temperature: {stats['max_temp']:.2f}°C")
    print(f"Minimum temperature: {stats['min_temp']:.2f}°C")
    print(f"Average humidity: {stats['avg_humidity']:.2f}%")

    print("\nExtreme days")
    print("-" * 30)
    print(f"Days >30°C: {extremes['hot_days']}")
    print(f"Days <10°C: {extremes['cold_days']}")
    print(f"Days >80% humidity: {extremes['humid_days']}")

    print("\nLast 5 days")
    print("-" * 30)
    for date, weather in list(month_data.items())[:5]:
        print(f"{date}: {weather['Temperature']}°C, {weather['Humidity']}% humidity")

    date, weather = hottest
    print("\nHottest day")
    print("-" * 30)
    print(f"{date}: {weather['Temperature']}°C, {weather['Humidity']}% humidity")


print("Generating fake weather data...")
time.sleep(1)

temp, humidity = generate_data()
stats = compute_stats(temp, humidity)
extremes = count_extremes(temp, humidity)
month_data = build_month_data(temp, humidity)
hottest = find_hottest_day(month_data)

print_report(stats, extremes, month_data, hottest)