from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")

csv_path = "<path_to_your_cleaned_data.csv>"
df = pd.read_csv(csv_path)

engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/{db}')
df.to_sql("retail_data_cleaned", engine, if_exists="replace", index=False)