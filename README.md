# Weather ETL Project

## Overview
This project implements an **ETL (Extract, Transform, Load)** pipeline that fetches weather data from an API, processes it (transforms the temperature to Celsius), and loads it into an **SQLite database**. The data includes weather details such as temperature, humidity, and wind speed for multiple cities.

## Features
- **Extract**: Fetches weather data from an external API (currently OpenWeatherMap) for multiple cities.
- **Transform**: Converts temperature from **Kelvin to Celsius** and flattens the nested data into a suitable format for loading into the database.
- **Load**: Loads the transformed data into an **SQLite database** (`weather_data.db`).
- Supports handling weather data for **multiple cities** (currently London, New York, Tokyo).

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


### Steps to Run the Project Locally

1. **Clone the Repository**:
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/Python-ETL.git
   cd Python-ETL
