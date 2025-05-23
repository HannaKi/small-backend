import duckdb
import pandas as pd


def load_all_data() -> pd.DataFrame:
    # Query from a CSV or other source
    df = duckdb.query(
        """
        SELECT *
        FROM read_csv_auto('data/1_hfp_from_mqtt.csv')
    """
    ).to_df()
    return df


def load_coordinate_data() -> pd.DataFrame:
    # Query from a CSV or other source
    df = duckdb.query(
        """
        SELECT route, dir, lat, long, spd
        FROM read_csv_auto('data/1_hfp_from_mqtt.csv')
    """
    ).to_df()
    return df
