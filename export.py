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

# SQL query to select data from the database table
sql_query = "SELECT * FROM sxr.LocationInfo"

# Execute the SQL query and create a DataFrame
df_exported = pd.read_sql(sql_query, con=engine)

# Specify the path where you want to export the DataFrame to a CSV file
exported_file_path = "D:/Location_Info.csv"

# Export the DataFrame to a CSV file
df_exported.to_csv(exported_file_path, index=False)

print(f'Data exported to CSV: {exported_file_path}')
