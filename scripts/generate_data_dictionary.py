import psycopg2
import pandas as pd

# Database connection
conn = psycopg2.connect(
    dbname="healthcare_db",
    user="postgres",
    password="Augustine123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Query to get column details
cur.execute("""
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'maternal_health_data';
""")

columns = cur.fetchall()

# Convert to DataFrame
data_dict = pd.DataFrame(columns, columns=["Column Name", "Data Type", "Is Nullable"])

# Save as Excel and JSON
data_dict.to_excel("maternal_health_data_dictionary.xlsx", index=False)
data_dict.to_json("maternal_health_data_dictionary.json", orient="records", indent=4)

print("✅ Data Dictionary Created Successfully!")

# Close connection
cur.close()
conn.close()