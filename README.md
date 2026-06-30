# 🌦️ Weather Data Analysis Tool

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![NumPy](https://img.shields.io/badge/numpy-required-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A simple Python script that simulates 30 days of daily temperature and humidity data, computes summary statistics, identifies extreme weather days, and prints a formatted report to the console.

## 📋 Table of Contents

- [Features](#-features)
- [What Makes It Unique](#-what-makes-it-unique)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Project Structure](#-project-structure)
- [Notes](#-notes)
- [License](#-license)

## ✨ Features

- **Synthetic data generation** — creates 30 days of fake temperature (°C) and humidity (%) readings using a normal distribution, clipped to realistic ranges.
- **Summary statistics** — average, maximum, and minimum temperature, plus average humidity.
- **Extreme day counts** — counts of hot days (>30°C), cold days (<10°C), and humid days (>80% humidity).
- **Daily breakdown** — maps each of the last 30 calendar dates to its temperature and humidity reading.
- **Hottest day lookup** — identifies the single hottest day in the dataset.
- **Console report** — prints a readable, sectioned summary of all the above.

## 🌟 What Makes It Unique

- **No external data dependency** — generates statistically realistic weather data on the fly, so the tool runs end-to-end with zero setup, API keys, or internet access.
- **Reproducible by design** — the optional `seed` parameter in `generate_data()` lets you regenerate the exact same "random" dataset, useful for testing or demos.
- **Realistic bounds, not raw randomness** — values are clipped to physically sensible ranges (-5°C to 45°C, 20%–100% humidity) instead of letting the normal distribution produce implausible outliers.
- **Clean functional decomposition** — each step (generate, compute stats, find extremes, build daily map, find hottest day, report) is its own pure function, making the codebase easy to test, extend, or repurpose for real data sources.
- **NumPy-first approach** — built as a practical, hands-on demonstration of vectorized statistics (`np.average`, `np.clip`, boolean masking) rather than manual loops.

## 🔧 Requirements

- Python 3.7+
- [NumPy](https://numpy.org/)

## 📦 Installation

```bash
git clone https://github.com/rohanpawar23/weather-data-analysis-tool.git
cd weather-data-analysis-tool
pip install numpy
```

## 🚀 Usage

Run the script directly:

```bash
python Weather_Data_Analysis_Tool.py
```

## 📊 Sample Output

```
Generating fake weather data...

Past 30 Days Weather Report
------------------------------
Average temperature: 19.84°C
Maximum temperature: 38.21°C
Minimum temperature: -5.00°C
Average humidity: 59.67%

Extreme days
------------------------------
Days >30°C: 3
Days <10°C: 6
Days >80% humidity: 2

Last 5 days
------------------------------
2026-06-30: 21.45°C, 55.32% humidity
...

Hottest day
------------------------------
2026-06-18: 38.21°C, 47.10% humidity
```

## 🗂️ Project Structure

The script is organized into small, single-purpose functions:

| Function | Description |
|---|---|
| `generate_data(days=30, seed=None)` | Generates random temperature and humidity arrays. Accepts an optional `seed` for reproducible output. |
| `compute_stats(temp, humidity)` | Returns a dictionary of average/max/min temperature and average humidity. |
| `count_extremes(temp, humidity)` | Returns a dictionary of counts for hot, cold, and humid days. |
| `build_month_data(temp, humidity, days=30)` | Builds a dictionary mapping each of the past `days` dates to its temperature and humidity. |
| `find_hottest_day(month_data)` | Returns the `(date, weather)` entry with the highest temperature. |
| `print_report(stats, extremes, month_data, hottest)` | Prints the full formatted report to the console. |

## 📝 Notes

- Data is randomly generated on each run unless a `seed` is passed to `generate_data()`, so output will differ between executions.
- Temperature values are clipped to a range of -5°C to 45°C; humidity is clipped to 20%–100%.
- Dates in `month_data` are calculated relative to the current system date, counting backward from today.

## 📄 License

This project is licensed under the MIT License.

---

**Author:** [Rohan Pawar](https://github.com/rohanpawar23)
