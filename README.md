# Sales Data Heatmap Generation Project

This is a Python project to generate a heatmap from sales data obtained from a PostgreSQL database. The objective is to visualize the geographical distribution of sales within a certain time period.

## Project Structure

The project is structured as follows:

- **`src/`**: Contains the project modules.
    - **`db_connector.py`**: Class for connecting to and querying the PostgreSQL database.
    - **`geocoder.py`**: Class for geocoding the ZIP codes using the Nominatim API.
    - **`heatmap_generator.py`**: Class for generating the heatmap from the geographical data.
    - **`api_cep.py`**: Class that queries the VIACEP API and obtains the necessary data to perform the query, in case the ZIP code alone is not sufficient for this.
    - **`format_df.py`**: Formats the DataFrame as needed. It comes with default rules, but they can be easily changed.
- **`main.py`**: Entry point of the program, where execution starts..

## How to Run

1. Make sure you have Python installed on your machine.
2. Install the project dependencies by running the following command in the terminal:

    ```
    pip install psycopg2 folium geopy requests
    ```

3. In the `main.py` file, set the PostgreSQL database connection settings in the "Connection Settings" section.
4. Execute the `main.py` file:

    ```
    python main.py
    ```

5. The heatmap will be generated and saved as `heatmap.html` in the current directory.

## Configuration

In the `main.py` file, you can set the following configurations:

- `db_host`: IP address or hostname of the PostgreSQL database.
- `db_port`: Port of the PostgreSQL database.
- `db_database`: Name of the PostgreSQL database.
- `db_user`: Username for authentication to the PostgreSQL database.
- `db_password`: Password for authentication to the PostgreSQL database.

## Contributing

Contributions are welcome! Feel free to open an issue to report bugs or suggest new features. Pull requests are also appreciated.
