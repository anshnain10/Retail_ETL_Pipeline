import pandas as pd
from sqlalchemy import create_engine

csv_path = "/Users/ansh/etl-pipeline/output/cleaned_data/cleaned_data.csv"
df = pd.read_csv(csv_path)

# ✅ Use credentials from docker-compose.yml
user = "retail_user"
password = "retail_pass"     # <- use the actual password you set
host = "localhost"
port = "5432"
database = "retail_db"

# SQLAlchemy connection string
url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(url)

df.to_sql("retail_data_cleaned", engine, if_exists="replace", index=False)
print("✅ Data inserted into PostgreSQL successfully!")
