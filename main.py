try:
    import pandas as pd
except Exception as e:
    print(f"Lib not installed: %s" % e)
from src.config import DB_HOST, DB_PORT, DB_DATABASE, DB_USER, DB_PASSWORD
from src.db_connector import DBConnector
from src.geolocation import Geocoder
from src.heatmap_generator import HeatmapGenerator
from src.format_csv import DataframeFormatter


# Create your query here
consulta_sql = '''
    SELECT cep,name,id_sale_order FROM table WHERE id = x
'''

try:
    # Create a connection to the database by passing the parameters
    connector = DBConnector(DB_HOST, DB_PORT, DB_DATABASE, DB_USER, DB_PASSWORD)
    connector.connect()

    # Executes the SQL query and loads the data into a Pandas lib DataFrame
    df = pd.read_sql_query(consulta_sql, connector.conn).astype(int)

    # After querying the data, close the connection to the DB
    connector.disconnect()

    # Instantiate the Geocoder
    geocoder = Geocoder()

    # Instantiate the DataframeFormatter
    df_formatt = DataframeFormatter()

    # Check zip codes and add an extra number if missing
    df['cep'] = df['cep'].apply(geocoder.zip_adjust)

    # Geocodes zip codes and adds the coordinate column to the DataFrame
    df['coordinates'] = df['cep'].apply(geocoder.geocode)

    df = df_formatt.format_dataframe(input_file=df)

    # For eventual use of the CSV instead of doing the process again
    df.to_csv("backup_df.csv", index=False)

    # Remove lines with empty coordinates
    df.dropna(subset=['coordinates'], inplace=True)

    heatmap_generator = HeatmapGenerator(df)
    heatmap_generator.generate_heatmap()

except Exception as e:
    print(f"Error: {str(e)}")
