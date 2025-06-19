from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_data_to_db

# Step 1: Extract data
raw_data = extract_weather_data('London')

# Step 2: Transform data
transformed_data = transform_weather_data(raw_data)

# Step 3: Load data to the database
load_data_to_db(transformed_data)

print("ETL pipeline completed successfully!")
