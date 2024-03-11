from sqlalchemy import create_engine
import pandas as pd

# Database connection configuration
db_config = {
    'server': 'ATISL235',
    'database': 'Test',
    'trusted_connection': 'yes',
    'driver': 'ODBC Driver 17 for SQL Server',
}

# Create SQLAlchemy engine
engine = create_engine('mssql+pyodbc://' + db_config['server'] +
                       '/' + db_config['database'] +
                       '?trusted_connection=' + db_config['trusted_connection'] +
                       '&driver=' + db_config['driver'])

# Specify the path of the CSV file to be imported
imported_file_path = "D:/2m Sales Records.csv"

# Specify the table name in the database where you want to import the data
table_name = "2m Sales Records"

# Define chunk size (adjust as needed)
chunk_size = 1000

# Create an iterator for reading the CSV file in chunks
csv_reader = pd.read_csv(imported_file_path, chunksize=chunk_size, iterator=True)

# Iterate over chunks and import into SQL Server
for i, chunk in enumerate(csv_reader):
    # Replace NaN values with None for proper handling in SQL Server
    chunk = chunk.where(pd.notna(chunk), None)

    # Import the chunk into the SQL Server database table
    if i == 0:
        chunk.to_sql(table_name, con=engine, if_exists='replace', index=False)
    else:
        chunk.to_sql(table_name, con=engine, if_exists='append', index=False)

print(f'Data imported to SQL Server table: {table_name}')
