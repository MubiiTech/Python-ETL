# Weather ETL Project

## Overview
This project is a **Weather ETL (Extract, Transform, Load) pipeline** that fetches weather data from an API, processes it, and loads it into an SQLite database. The data includes information like temperature, humidity, wind speed, and more for different cities. The project follows a modular approach, with separate scripts for data extraction, transformation, and loading.

## What Does It Do?
This project performs the following steps:
1. **Extract**: Fetches weather data from an external weather API (OpenWeatherMap).
2. **Transform**: Converts the temperature from Kelvin to Celsius and flattens the nested data into a more suitable format for database storage.
3. **Load**: Inserts the processed data into an SQLite database (`weather_data.db`), where the weather information is stored in a table.

## Features
- Extracts weather data for cities (currently supports fetching data for one city, e.g., London).
- Transforms the temperature from Kelvin to Celsius.
- Stores the transformed data in a local SQLite database (`weather_data.db`).
- Modular ETL pipeline with separate scripts for **Extract**, **Transform**, and **Load**.

## Tech Stack
This project uses the following technologies and libraries:

- **Python 3.x**: Programming language used for writing the ETL scripts.
  - Version: `3.8` or higher
- **Pandas**: Data manipulation and transformation library.
  - Version: `2.3.0`
- **Requests**: Library for making HTTP requests to interact with the weather API.
  - Version: `2.32.4`
- **SQLAlchemy**: ORM to interact with SQLite for loading data.
  - Version: `2.0.41`
- **SQLite**: Database used for storing the transformed weather data.
  - Version: `3.x`
- **python-dotenv**: For managing environment variables (e.g., API keys).
  - Version: `0.21.0`

## How to Run and Test Locally

### Prerequisites
1. **Python 3.x** should be installed on your local machine.
2. A **weather API key** (e.g., from [OpenWeatherMap](https://openweathermap.org/)).

### Steps to Run the Project Locally

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/Python-ETL.git
   cd Python-ETL
