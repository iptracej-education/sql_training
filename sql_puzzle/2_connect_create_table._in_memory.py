import sqlite3
import pandas as pd

# =============================================================================
# PREREQUISITES: SETUP DATA AND DATABASE
# =============================================================================

# --- Create an in-memory SQLite database for SQL exercises ---
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a sample table "data" (for complaints)
cursor.execute("DROP TABLE IF EXISTS data;")
cursor.execute("""
CREATE TABLE data (
    ComplaintType TEXT,
    City TEXT,
    CreatedDate TEXT
);
""")
# Insert sample data (note: ComplaintType and City use different cases)
complaints_sample = [
    ('Noise', 'new york', '2022-01-01 12:00:00.0'),
    ('noise', 'NEW YORK', '2022-01-02 14:00:00.0'),
    ('Plumbing', 'Brooklyn', '2022-01-03 09:00:00.0'),
    ('Street Light', 'bronx', '2022-01-04 18:00:00.0'),
    ('Noise', 'New York', '2022-01-05 11:00:00.0'),
    ('Noise', 'Queens', '2022-01-06 10:00:00.0')  # This row may be filtered later.
]
cursor.executemany("INSERT INTO data (ComplaintType, City, CreatedDate) VALUES (?, ?, ?);", complaints_sample)
conn.commit()

# Read the data in data table
df = pd.read_sql_query("SELECT * FROM data",conn)
print(df)

conn.close()

