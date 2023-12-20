import os
import pandas as pd
import geopandas as gpd


def geojson_to_csv(geojson_path, csv_path):
    """
    Converts a GeoJSON file to a CSV file.
    """
    # Load GeoJSON file
    gdf = gpd.read_file(geojson_path)

    # Convert GeoDataFrame to DataFrame
    df = pd.DataFrame(gdf.drop(columns='geometry'))

    # Save to CSV
    df.to_csv(csv_path, index=False)


def main():
    geojson_folder = './data_files'
    csv_folder = './csv-files'

    # Create the CSV folder if it doesn't exist
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    # Process each GeoJSON file in the folder
    for file in os.listdir(geojson_folder):
        if file.endswith('.geojson'):
            geojson_path = os.path.join(geojson_folder, file)
            csv_path = os.path.join(csv_folder, file.replace('.geojson', '.csv'))
            geojson_to_csv(geojson_path, csv_path)
            print(f'Converted {file} to CSV.')


if __name__ == '__main__':
    main()
