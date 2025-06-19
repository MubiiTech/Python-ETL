from sqlalchemy import create_engine

def load_data_to_db(df):
    engine = create_engine('sqlite:///weather_data.db')
    df.to_sql('weather', engine, if_exists='replace', index=False)

# Example of loading data to the database
if __name__ == "__main__":
    import pandas as pd
    data = {
        "city": ["London"],
        "temp_celsius": [20.0],
        "humidity": [80]
    }
    df = pd.DataFrame(data)
    load_data_to_db(df)
